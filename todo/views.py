from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import CusUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def test_home(request):
    form = CusUserCreationForm()
    return render(request,'todo/home.html',{"form":form})

def register_user(request):
    if request.method == 'POST':
        form = CusUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CusUserCreationForm()
    return render(request,'todo/register.html',{"form":form})



