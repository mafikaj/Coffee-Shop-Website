# lunalatte/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import MenuItem
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect

# lunalatte/views.py


def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'home.html', {'menu_items': menu_items})


def about(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle the form submission (e.g., send email, save to database)
            # Redirect to a thank-you page or homepage after submission
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')
