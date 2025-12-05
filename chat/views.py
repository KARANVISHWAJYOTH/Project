from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from listings.models import Listing
from .models import Message
from .forms import MessageForm


@login_required
def chat_list(request):
    """Show list of conversations"""
    # Get all unique users the current user has chatted with
    sent_messages = Message.objects.filter(sender=request.user).values_list('receiver', flat=True).distinct()
    received_messages = Message.objects.filter(receiver=request.user).values_list('sender', flat=True).distinct()
    user_ids = set(list(sent_messages) + list(received_messages))
    users = User.objects.filter(id__in=user_ids)
    
    # Get last message for each conversation
    conversations = []
    for user in users:
        last_message = Message.objects.filter(
            Q(sender=request.user, receiver=user) | Q(sender=user, receiver=request.user)
        ).order_by('-sent_at').first()
        conversations.append({
            'user': user,
            'last_message': last_message
        })
    
    conversations.sort(key=lambda x: x['last_message'].sent_at if x['last_message'] else None, reverse=True)
    
    return render(request, 'chat/chat_list.html', {'conversations': conversations})


@login_required
def chat_detail(request, user_id, listing_id=None):
    """Chat with a specific user about a listing"""
    other_user = get_object_or_404(User, pk=user_id)
    listing = None
    
    if listing_id:
        listing = get_object_or_404(Listing, pk=listing_id)
    
    # Get all messages between current user and other user
    chat_messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) | Q(sender=other_user, receiver=request.user)
    ).order_by('sent_at')
    
    # Mark messages as read
    Message.objects.filter(sender=other_user, receiver=request.user, is_read=False).update(is_read=True)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = other_user
            message.listing = listing
            message.save()
            messages.success(request, 'Message sent!')
            if listing_id:
                return redirect('chat:chat_detail_with_listing', user_id=user_id, listing_id=listing_id)
            else:
                return redirect('chat:chat_detail', user_id=user_id)
    else:
        form = MessageForm()
    
    return render(request, 'chat/chat_detail.html', {
        'other_user': other_user,
        'listing': listing,
        'messages': chat_messages,
        'form': form
    })


@login_required
def start_chat(request, listing_id):
    """Start a chat with the owner of a listing"""
    listing = get_object_or_404(Listing, pk=listing_id)
    
    if listing.owner == request.user:
        messages.error(request, 'You cannot chat with yourself!')
        return redirect('listings:listing_detail', pk=listing_id)
    
    return redirect('chat:chat_detail_with_listing', user_id=listing.owner.id, listing_id=listing_id)

