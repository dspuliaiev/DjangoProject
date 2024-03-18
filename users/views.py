from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


def signupuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Створюємо профіль юзера
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('quotes:root')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            return redirect('quotes:root')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logoutuser(request):
    logout(request)
    return redirect('quotes:root')
