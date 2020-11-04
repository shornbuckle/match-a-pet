from django.urls import path
from . import views
from .views import PetListView

# from django.contrib.auth import login
# from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import VerificationView

app_name = "accounts"
urlpatterns = [
    path("", views.home, name="accounts-home"),
    path("register/shelter/", views.registerShelter, name="register-shelter"),
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
    path("activate/<uidb64>/<token>", VerificationView.as_view(), name="activate"),
    path("pets/view_pets/", PetListView.as_view(), name="view-pets"),
    path("pets/<id>/", views.petProfile, name="pet-profile"),
    path("profile/<username>/", views.shelter_profile, name="shelterprofile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
