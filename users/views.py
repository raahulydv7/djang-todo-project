from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import CusUserCreationForm,CusAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def register_user(request):
    if request.method == 'POST':
        form = CusUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todos')
    else:
        form = CusUserCreationForm()
    return render(request,'users/register.html',{"form":form})


def login_user(request):
    if request.method == 'POST':
        form = CusAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todos')
    else:
        form = CusAuthenticationForm() 
    
    return render(request, 'users/login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('login')