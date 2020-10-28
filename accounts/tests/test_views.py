from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import ShelterRegisterData, Pet


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

    def test_shelter_register_post_view(self):
        client = Client()
        self.dummy_user = ShelterRegisterData.objects.create(
            shelter_id=5,
            username="peter7",
            email="peter@matchapet.com",
            first_name="Peter",
            last_name="Voltz",
            shelter_city="Manhattan",
            shelter_state="New York",
            password="test123abc",
        )

        response = client.post(reverse("accounts:register-shelter"), {})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")
        self.assertEquals(str(self.dummy_user.email), "peter@matchapet.com")
        self.assertEquals(str(self.dummy_user.username), "peter7")
        self.assertEquals(str(self.dummy_user.first_name), "Peter")
        self.assertEquals(str(self.dummy_user.last_name), "Voltz")
        self.assertEquals(str(self.dummy_user.shelter_state), "New York")

    def test_shelter_register_post_view1(self):
        client = Client()
        self.registerURL = reverse("accounts:register-shelter")
        self.dummy_user = ShelterRegisterData.objects.create(
            shelter_id=5,
            username="peter7",
            email="peter@matchapet.com",
            first_name="Peter",
            last_name="Voltz",
            shelter_city="Manhattan",
            shelter_state="New York",
            password="test123abc",
        )

        response = client.post(
            self.registerURL,
            {
                "username": "peter7",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
                "shelter_city": "Manhattan",
                "shelter_state": "New York",
                "password1": "test123abc",
                "password2": "test123abc",
            },
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")
        self.assertEquals(str(self.dummy_user.email), "peter@matchapet.com")
        self.assertEquals(str(self.dummy_user.username), "peter7")
        self.assertEquals(str(self.dummy_user.first_name), "Peter")
        self.assertEquals(str(self.dummy_user.last_name), "Voltz")
        self.assertEquals(str(self.dummy_user.shelter_state), "New York")

    def test_shelter_update_post_view1(self):
        client = Client()
        self.registerURL = reverse("accounts:shelter-profile")
        self.dummy_user = ShelterRegisterData.objects.create(
            shelter_id=5,
            username="peter7",
            email="peter@matchapet.com",
            first_name="Peter",
            last_name="Voltz",
            shelter_city="Manhattan",
            shelter_state="New York",
            password="test123abc",
        )

        shelterid = ShelterRegisterData.objects.get(shelter_id=5)

        response = client.post(self.registerURL, {})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(shelterid.username, "peter7")
        self.assertEquals(shelterid.email, "peter@matchapet.com")
        self.assertEquals(str(self.dummy_user.email), "peter@matchapet.com")
        self.assertEquals(str(self.dummy_user.username), "peter7")
        self.assertEquals(str(self.dummy_user.first_name), "Peter")
        self.assertEquals(str(self.dummy_user.last_name), "Voltz")
        self.assertEquals(str(self.dummy_user.shelter_state), "New York")

    def test_pet_register_post_view(self):
        client = Client()
        self.dummy_user = ShelterRegisterData.objects.create(
            email="peter@matchapet.com",
        )
        self.dummy_pet = Pet.objects.create(
            email=self.dummy_user,
            pet_id="5",
            pet_name="Sheila",
            pet_breed="Dog",
            pet_age="4",
            pet_color="White",
            pet_gender="Female",
            date_entered="12/1/2020",
        )

        petid = Pet.objects.get(pet_id=5)
        # shelterid = ShelterRegisterData.objects.get(shelter_id=5)

        response = client.post(reverse("accounts:pet-register"), {})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(str(petid.email), "peter@matchapet.com")
        self.assertTemplateUsed(response, "accounts/pets.html")
        self.assertEquals(str(self.dummy_pet.email), "peter@matchapet.com")

    # def test_pet_register_post_view1(self):
    #     client = Client()
    #     self.dummy_user = ShelterRegisterData.objects.create(
    #         email="peter@matchapet.com",
    #     )
    #     self.dummy_pet = Pet.objects.create(
    #         email=self.dummy_user,
    #         pet_id="5",
    #         pet_name="Sheila",
    #         pet_breed="Dog",
    #         pet_age="4",
    #         pet_color="White",
    #         pet_gender="Female",
    #         date_entered="12/1/2020",
    #     )

    #     response = client.post(reverse("accounts:pet-register"), {
    #         "email":"peter@matchapet.com",
    #         "pet_name": "Sheila",
    #         "pet_breed": "Dog",
    #         "pet_age": "4",
    #         "pet_color": "White",
    #         "pet_gender": "Female",
    #         "date_entered": "12/1/2020",
    #     })
    #     print(response)
    #     print(self.dummy_pet.email)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, "accounts/pets.html")
    #     self.assertEquals(str(self.dummy_pet.email), "peter@matchapet.com")
    #     self.assertEquals(self.dummy_pet.pet_name, "pet_name")
