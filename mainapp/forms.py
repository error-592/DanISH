from django import forms
from .models import Profile, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )
    
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.'
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text=(
            'Your password can’t be too similar to your other personal information.<br>'
            'Your password must contain at least 8 characters.<br>'
            'Your password can’t be a commonly used password.<br>'
            'Your password can’t be entirely numeric.'
        )
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        help_text='Enter the same password as before, for verification.'
    )


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Replace with your custom user model
        fields = ('username', 'password')

    error_messages = {
        'invalid_login': (
            "The username or password you entered is incorrect. Please try again."
        ),
        'inactive': ("This account is inactive."),
    }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']


class CustomPasswordChangeForm(PasswordChangeForm):
    pass