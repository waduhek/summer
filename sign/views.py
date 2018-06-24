from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

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
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)

    return redirect('/')
