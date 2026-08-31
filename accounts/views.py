from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import AbstractUser
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-user')
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {
        'form': form
    })

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username = data["username"],
                password = data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("homepage")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {
        'form': form
    })

def logout_user(request):
    logout(request)
    return redirect("homepage")

