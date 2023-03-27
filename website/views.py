from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()

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
        return render(request, 'website/home.html', {'records': records})

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
        

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(pk=pk)
        return render(request, 'website/record.html', {'record': customer_record})
    else:
        messages.success(request, "You Must Be Logged In to View This Record", extra_tags='secondary')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(pk=pk)
        delete_it.delete()
        messages.success(request, "Records Deleted Successfully", extra_tags='danger')
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In to View This Record", extra_tags='secondary')
        return redirect('home')