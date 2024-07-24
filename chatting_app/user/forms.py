from django import forms

from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-inputs', 'id': 'password', 'placeholder': 'Your Password'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'John Smith', 'class': 'form-inputs'}),
            'email': forms.TextInput(attrs={'placeholder': 'johnsmith@gmail.com', 'class': 'form-inputs'})
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password'
        }