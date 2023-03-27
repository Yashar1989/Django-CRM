from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password", extra_tags='danger')
            return redirect('home')
    else:
        return render(request, 'website/home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome")
            return redirect('home')
    else:
        form = SignUpForm()       
        return render(request, 'website/register.html', {'form': form})
    return render(request, 'website/register.html', {'form': form})
        
        