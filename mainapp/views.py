from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileForm
from .models import Profile, CustomUser


def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)
        
            login(request, user) # Log the user in
            return redirect('mainapp:login')  # sends user to "the" page after complition of registration
        else:
            messages.error(request, 'Error creating the account. Please check the form data.')
    else:
        form = CustomUserCreationForm() #important 
    return render(request, 'registration/signup.html', {'form': form})

# @login_required
# def user_profile(request):
#     user = request.user
#     context = {
#         'user': user,
#     }
#     return render(request, 'registration/profile.html')
   

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile  # Set the model to Profile
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('mainapp:profile-update')  # Update the success URL

    def get_object(self, queryset=None):
        # Get the profile of the currently logged-in user
        return self.request.user.profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Include the user object in the context
        return context
    

class ProfilePictureUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_picture_form.html'  # gotta make a template of the same name as this
    success_url = reverse_lazy('mainapp:profile-update')


@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('mainapp:profile-update')  # Redirect to the profile update page
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {
        'form': form,
        'user': request.user,  # Include the user object in the context
    }
    

    return render(request, 'profile_picture_form.html', {'form': form})    