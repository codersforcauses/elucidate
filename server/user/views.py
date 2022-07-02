from django import forms
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print(form.data)
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('/')  # Change this after
    else:
        form = CreateUserForm()
        
    return render(request, 'register.html', {'form': form})
