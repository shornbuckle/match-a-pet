from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import registerShelter, shelterProfile, petsRegister
from django.contrib.auth.views import LoginView, LogoutView


class TestUrls(SimpleTestCase):
    def test_shelter_register_url(self):
        url = reverse("accounts:register-shelter")
        self.assertEquals(resolve(url).func, registerShelter)
        self.assertEquals(resolve(url).route, "register/shelter/")

    def test_shelter_login_url(self):
        url = reverse("accounts:login-shelter")
        self.assertEquals(resolve(url).func.view_class, LoginView)
        self.assertEquals(resolve(url).route, "login/shelter/")

    def test_shelter_logout_url(self):
        url = reverse("accounts:logout-shelter")
        self.assertEquals(resolve(url).func.view_class, LogoutView)
        self.assertEquals(resolve(url).route, "logout/shelter/")

    def test_shelter_profile_url(self):
        url = reverse("accounts:shelter-profile")
        self.assertEquals(resolve(url).func, shelterProfile)
        self.assertEquals(resolve(url).route, "profile/shelter/")

    def test_pet_register_url(self):
        url = reverse("accounts:pet-register")
        self.assertEquals(resolve(url).func, petsRegister)
        self.assertEquals(resolve(url).route, "pets/register/")
