from django.urls import path
from . import views

# from django.contrib.auth import login
# from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
#from .views import VerificationView

#below are Sean Testing Views
from django.urls import include, path
from .views import accounts, shelters, users, testingviews


app_name = "accounts"
urlpatterns = [
    path("", accounts.home, name="accounts-home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.SignUpView.as_view(), name='signup'),
    path('accounts/signup/user/', users.ClientSignUpView.as_view(), name='ClientUser_signup'),
    path('accounts/signup/shelter/', shelters.ShelterSignUpView.as_view(), name='ShelterUser_signup'),
    path(
    "login/shelter/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login-shelter",
    ),
    path(
        "logout/shelter/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout-shelter",
    ),
    #path("pets/register/", shelters.petsRegister, name="pet-register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""

    path("", views.home, name="accounts-home"),
    path("register/shelter/", views.registerShelter, name="register-shelter"),
    path("register/user/", views.registerUser, name="register-user"),
    path(
        "login/shelter/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login-shelter",
    ),
    path(
        "logout/shelter/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout-shelter",
    ),
    path("profile/shelter/", views.shelterProfile, name="shelter-profile"),
    path("pets/register/", views.petsRegister, name="pet-register"),
    #path("activate/<uidb64>/<token>", VerificationView.as_view(), name="activate"),
    #path('', include('classroom.urls')),

"""
