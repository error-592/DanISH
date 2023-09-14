from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in
            return redirect('registration/login.html')  # sends user to "the" page after complition of registration
        else:
            messages.error(request, 'Error creating the account. Please check the form data.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def user_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'registration/profile.html')
   