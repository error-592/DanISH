from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from mainapp.views import CustomLoginView

app_name = 'mainapp'

urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'), # Homepage
    path('profile/', views.user_profile, name='user_profile'),

]