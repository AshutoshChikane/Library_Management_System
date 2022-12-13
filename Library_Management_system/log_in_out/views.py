from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import new_user, log_in
from django.contrib.auth.models import User

# Create your views here.


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('addbooks')
    if request.method == "POST":
        fm = new_user(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "User Created Successfully!!")
            fm = new_user()
    else:
        fm = new_user()
    return render(request, "signup.html", {'fm': fm})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('addbooks')
    if request.method == "POST":
        fm = log_in(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            print("user", user)
            if user is not None:
                login(request, user)
                messages.success(request, "login successfull!!")
                return redirect("addbooks")
    else:
        fm = log_in()
    return render(request, "login.html", {'fm': fm})


def logoutt(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, message="logout successfull!!")
    return redirect("signin")
