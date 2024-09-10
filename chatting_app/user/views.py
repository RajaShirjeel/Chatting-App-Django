from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import CustomUserForm, LoginForm
# Create your views here.

def signup_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('user:login_user')
    
    else:
        form = CustomUserForm()
    
    return render(request, 'user/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password) 
            if user is not None:
                login(request, user)
                return redirect('interaction:all_chats')

            else:
                form.add_error('email', 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form' : form})


def logout_user(request):
    logout(request)
    return redirect('user:signup_user')
