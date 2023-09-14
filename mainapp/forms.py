from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Replace with your custom user model
        fields = ('username', 'password1', 'password2')  # Customize as needed

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Replace with your custom user model
