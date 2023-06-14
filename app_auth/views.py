from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from app_auth.forms import LoginForm

def login_confidenz(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})            