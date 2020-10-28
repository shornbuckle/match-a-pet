from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_home_view(self):
        client = Client()

        response = client.get(reverse("accounts:accounts-home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/home.html")

    def test_shelter_register_view(self):
        client = Client()

        response = client.get(reverse("accounts:register-shelter"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_shelter_login_view(self):
        client = Client()

        response = client.get(reverse("accounts:login-shelter"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_shelter_logout_view(self):
        client = Client()

        response = client.get(reverse("accounts:logout-shelter"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/logout.html")

    def test_shelter_profile_view(self):
        client = Client()

        response = client.get(reverse("accounts:shelter-profile"))
        self.assertEquals(response.status_code, 302)

    def test_pet_register_view(self):
        client = Client()

        response = client.get(reverse("accounts:pet-register"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pets.html")
