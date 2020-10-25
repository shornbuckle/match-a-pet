from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from .views import PetListView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='accounts-home'),
    path('register/shelter/', views.registerShelter, name='register-shelter'),
    path('register/user/', views.registerUser, name='register-user'),
    path('login/shelter/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login-shelter'),
    path('logout/shelter/', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout-shelter'),
    path('profile/shelter/', views.shelterProfile, name='shelter-profile'),
    path('pets/register/', views.petsRegister, name='pet-register'),
    #path('pets/view_pets/', views.PetListView, name='pet-view_pets'),
    path("pets/view_pets/", PetListView.as_view())
]
