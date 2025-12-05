from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm


def welcome(request):
    """Welcome page with login and signup"""
    if request.user.is_authenticated:
        return redirect('listings:home')
    
    login_form = LoginForm()
    signup_form = SignUpForm()
    
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome back, {username}!')
                    return redirect('listings:home')
                else:
                    messages.error(request, 'Invalid username or password.')
        elif 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                messages.success(request, f'Account created successfully! Welcome, {user.username}!')
                return redirect('listings:home')
    
    return render(request, 'accounts/welcome.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })


@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('accounts:welcome')
