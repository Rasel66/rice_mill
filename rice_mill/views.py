from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomAuthenticationForm, CustomUserCreationForm

# Create your views here.

def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration Successfull!!!")
            return redirect("login")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/register.html', context)

def login_view(request):
    form = CustomAuthenticationForm()
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home_page")
        else:
            print(form.errors)
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page_view(request):
    return render(request, "home_page.html")