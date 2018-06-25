from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from . import forms

def signup(request):
    if request.method == 'POST':
        form = forms.SignUp(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('/')
    else:
        form = forms.SignUp()
    return render(request, 'sign/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = forms.Login(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
                return redirect('/')

            else:
                messages.error(request, 'Entered username or password is incorrect')

    else:
        form = forms.Login()

    return render(request, 'sign/login.html', {'form': form})

def logout_view(request):
    logout(request)

    return redirect('/')
