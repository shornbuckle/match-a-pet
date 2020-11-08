from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import registerShelter, shelterProfile, petsRegister, PetListView
from django.contrib.auth.views import LoginView, LogoutView


class TestUrls(SimpleTestCase):
    def test_shelter_register_url(self):
        url = reverse("accounts:register-shelter")
        self.assertEquals(resolve(url).func, registerShelter)
        self.assertEquals(resolve(url).route, "shelter/register/")

    def test_shelter_register_url(self):
        url = reverse("accounts:register-user")
        self.assertEquals(resolve(url).func, registerShelter)
        self.assertEquals(resolve(url).route, "user/register/")

    def test_shelter_login_url(self):
        url = reverse("accounts:login")
        self.assertEquals(resolve(url).func.view_class, LoginView)
        self.assertEquals(resolve(url).route, "login/")

    def test_shelter_logout_url(self):
        url = reverse("accounts:logout")
        self.assertEquals(resolve(url).func.view_class, LogoutView)
        self.assertEquals(resolve(url).route, "logout/")

    def test_shelter_profile_url(self):
        url = reverse("accounts:shelter-profile")
        self.assertEquals(resolve(url).func, shelterProfile)
        self.assertEquals(resolve(url).route, "shelter/profile/")

    def test_pet_register_url(self):
        url = reverse("accounts:pet-register")
        self.assertEquals(resolve(url).func, petsRegister)
        self.assertEquals(resolve(url).route, "pets/register/")

    def test_pets_view_url(self):
        url = reverse("accounts:view-pets")
        self.assertEquals(resolve(url).func.view_class, PetListView)
        self.assertEquals(resolve(url).route, "pets/view_pets/")
