"""
Module to define views of app 'authenication'.
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from authentication.forms import LoginForm

def login_page(request):
    """
    View to handle login page.
    """
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = "Identifiants invalides!"
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', context={
        'form': form,
        'message': message,
    })

@login_required
def logout_user(request):
    """
    Logout the current connected user.
    """
    logout(request)
    return redirect('login')