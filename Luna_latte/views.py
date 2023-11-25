# lunalatte/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import MenuItem
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect


def home(request):
    """
    Render the home page with a list of menu items.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML page with a list of menu items.
    """
    menu_items = MenuItem.objects.all()
    return render(request, 'home.html', {'menu_items': menu_items})


def about(request):
    """
    Render the about page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML page for the about section.
    """
    return render(request, 'about.html')


def contact_view(request):
    """
    Render and handle the contact form.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is POST and the form is valid, handle the form submission.
    - Rendered HTML page with the contact form.
    """
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
    """
    Render and handle the user signup form.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is POST and the form is valid, create a new user and log in.
    - Rendered HTML page with the signup form.
    """
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
    """
    Render and handle the user login form.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is POST and the form is valid, log in the user.
    - Rendered HTML page with the login form.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    """
    Log out the user.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Redirect to the home page after logging out the user.
    """
    auth_logout(request)
    return redirect('home')
