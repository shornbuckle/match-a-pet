from django.urls import path
from . import views
from django.contrib.auth import login

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='accounts-home'),
    path('register/shelter/', views.registerShelter, name='register-shelter'),
    path('register/user/', views.registerUser, name='register-user'),
    path('login/shelter/', views.loginShelter, name='login-shelter'),
]
