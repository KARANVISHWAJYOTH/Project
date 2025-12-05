from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Listing, Category, SearchHistory
from .forms import ListingForm, SearchForm
from .services import fetch_external_products
from .image_search import search_images


def home(request):
    """Homepage showing all categories"""
    if not request.user.is_authenticated:
        return redirect('accounts:welcome')
    
    categories = Category.objects.all()
    return render(request, 'listings/home.html', {'categories': categories})


def category_listings(request, slug):
    """Show all listings in a specific category"""
    if not request.user.is_authenticated:
        return redirect('accounts:welcome')
    
    category = get_object_or_404(Category, slug=slug)
    listings = Listing.objects.filter(category=category, is_sold=False).order_by('-created_at')

    # Fetch related visuals for this category (for richer browsing)
    image_matches = search_images(category.name, limit=8)
    
    # Pagination
    paginator = Paginator(listings, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'listings/category_listings.html', {
        'category': category,
        'listings': page_obj,
        'page_obj': page_obj,
        'image_matches': image_matches,
    })


def listing_detail(request, pk):
    """Show details of a specific listing"""
    if not request.user.is_authenticated:
        return redirect('accounts:welcome')
    
    listing = get_object_or_404(Listing, pk=pk)
    related_listings = Listing.objects.filter(
        category=listing.category,
        is_sold=False
    ).exclude(pk=pk)[:4]
    
    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'related_listings': related_listings
    })


@login_required
def create_listing(request):
    """Create a new listing"""
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            messages.success(request, 'Listing created successfully!')
            return redirect('listings:listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    
    return render(request, 'listings/create_listing.html', {'form': form})


@login_required
def edit_listing(request, pk):
    """Edit an existing listing"""
    listing = get_object_or_404(Listing, pk=pk)
    
    # Check if user owns the listing
    if listing.owner != request.user:
        messages.error(request, 'You do not have permission to edit this listing.')
        return redirect('listings:listing_detail', pk=pk)
    
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listing updated successfully!')
            return redirect('listings:listing_detail', pk=pk)
    else:
        form = ListingForm(instance=listing)
    
    return render(request, 'listings/edit_listing.html', {'form': form, 'listing': listing})


@login_required
def delete_listing(request, pk):
    """Delete a listing"""
    listing = get_object_or_404(Listing, pk=pk)
    
    # Check if user owns the listing
    if listing.owner != request.user:
        messages.error(request, 'You do not have permission to delete this listing.')
        return redirect('listings:listing_detail', pk=pk)
    
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Listing deleted successfully!')
        return redirect('listings:home')
    
    return render(request, 'listings/delete_listing.html', {'listing': listing})


def search_listings(request):
    """Search and filter listings"""
    if not request.user.is_authenticated:
        return redirect('accounts:welcome')
    
    form = SearchForm(request.GET)
    listings = Listing.objects.filter(is_sold=False).order_by('-created_at')
    searched_query = ''
    
    external_results = []
    image_matches = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        searched_query = query or ''
        
        # Apply filters
        if query:
            listings = listings.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        
        if category:
            listings = listings.filter(category=category)
        
        if min_price:
            listings = listings.filter(price__gte=min_price)
        
        if max_price:
            listings = listings.filter(price__lte=max_price)
        
        results_count = listings.count()
        # Save search history
        if request.user.is_authenticated:
            SearchHistory.objects.create(
                user=request.user,
                query=searched_query,
                category=category,
                min_price=min_price,
                max_price=max_price,
                results_count=results_count
            )
        if searched_query and results_count == 0:
            external_results = fetch_external_products(searched_query, limit=4)
            image_matches = search_images(searched_query, limit=6)
    else:
        results_count = listings.count()
    
    # Pagination
    paginator = Paginator(listings, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'listings/search_results.html', {
        'form': form,
        'listings': page_obj,
        'page_obj': page_obj,
        'searched_query': searched_query,
        'results_count': results_count,
        'external_results': external_results,
        'image_matches': image_matches,
    })


@login_required
def my_listings(request):
    """Show user's own listings"""
    listings = Listing.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'listings/my_listings.html', {'listings': listings})
