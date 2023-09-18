from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from mainapp.views import CustomLoginView, ProfileUpdateView

app_name = 'mainapp'

urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='mainapp:homepage'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'), # Homepage
    # path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('profile/update/', views.ProfilePictureUpdateView.as_view(), name='profile-update'),
    path('profile/upload/', views.upload_profile_picture, name='upload_profile_picture'),




]