from django.test import SimpleTestCase, TestCase
from accounts.forms import ShelterRegistrationForm, ShelterUpdateForm, PetForm
from django.urls import reverse
from accounts.models import ShelterRegisterData


class DefaultTestFroms(TestCase):
    def test_ShelterRegistrationForm_valid(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
                "shelter_city": "Manhattan",
                "shelter_state": "New York",
                "password1": "test123abc",
                "password2": "test123abc",
            }
        )

        self.assertTrue(form.is_valid())

    def test_ShelterRegistrationForm_no_data(self):
        form = ShelterRegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)

    def test_ShelterRegistrationForm_invalid_data(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

    def test_ShelterUpdateForm_valid(self):
        form = ShelterUpdateForm(
            data={
                "username": "peter3",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
                "shelter_city": "Brooklyn",
                "shelter_state": "New York",
            }
        )

        self.assertTrue(form.is_valid())

    def test_ShelterUpdateForm_no_data(self):
        form = ShelterUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_ShelterUpdateForm_invalid_data(self):
        form = ShelterUpdateForm(
            data={
                "username": "peter3",
                "email": "peter@matchapet.com",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


class TestForms(SimpleTestCase):
    def test_PetForm_valid(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
                "pet_breed": "Dog",
                "pet_age": "4",
                "pet_color": "White",
                "pet_gender": "Female",
                "date_entered": "12/1/2020",
            }
        )

        self.assertTrue(form.is_valid())

    def test_PetForm_no_data(self):
        form = PetForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_PetForm_invalid_data(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
                "pet_breed": "Dog",
                "pet_age": "4",
                "pet_color": "White",
                "pet_gender": "Female",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_PetForm_invalid_data1(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
                "pet_breed": "Dog",
                "pet_age": "4",
                "pet_color": "White",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_PetForm_invalid_data2(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
                "pet_breed": "Dog",
                "pet_age": "4",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_PetForm_invalid_data3(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
                "pet_breed": "Dog",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_PetForm_invalid_data4(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)


# ******


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse("accounts:register-shelter")
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

        self.user = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "shelter_city": "Manhattan",
            "shelter_state": "New York",
            "password1": "test123abc",
            "password2": "test123abc",
        }
        self.user_no_username = {
            "username": "",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "shelter_city": "Manhattan",
            "shelter_state": "New York",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_name_exists = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "shelter_city": "Manhattan",
            "shelter_state": "New York",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_email_exists = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "shelter_city": "Manhattan",
            "shelter_state": "New York",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_hm_invalid_email = {
            "username": "peter7",
            "email": "pet@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "shelter_city": "Manhattan",
            "shelter_state": "New York",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        return super().setUp


class RegisterFormTest(BaseTest):
    def test_form_not_valid(self):
        form = ShelterRegistrationForm(self.user_no_username)
        self.assertFalse(form.is_valid())

    def test_form_valid(self):
        form = ShelterRegistrationForm(self.user)
        self.assertFalse(form.is_valid())

    def test_form_username_exists(self):
        form = ShelterRegistrationForm(self.user_name_exists)
        form.has_error("username", "A user with that username already exists.")

    def test_form_email_exists(self):
        form = ShelterRegistrationForm(self.user_email_exists)
        form.has_error(
            "email",
            "This Email is already registered. "
            "Please use a different email address.",
        )

    def test_form_hm_invalid_email(self):
        form = ShelterRegistrationForm(self.user_hm_invalid_email)
        form.has_error(
            "This email is not a valid Email Address for Hiring Manager. "
            "Please use a different email address."
        )
