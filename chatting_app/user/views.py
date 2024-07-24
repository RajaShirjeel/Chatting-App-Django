from django.shortcuts import render
from django.contrib.auth import login

from .forms import CustomUserForm
# Create your views here.

def signup_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
    
    else:
        form = CustomUserForm()
    
    return render(request, 'user/signup.html', {'form': form})


def login_user(request):
    pass