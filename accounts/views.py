from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import CustomUserCreationForm
from accounts.forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})




def login_view(request):
    form = LoginForm(request.POST or None)
    error = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = "Invalid username or password."

    return render(request, 'login.html', {'form': form, 'error': error})
