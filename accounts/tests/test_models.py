from django.test import TestCase
from django.urls import reverse
from accounts.models import ShelterRegisterData, Pet, UserRegisterData, User
from accounts.forms import (
    ShelterRegistrationForm,
    PetForm,
    UserRegistrationForm,
    ShelterUserUpdateForm,
    ShelterUpdateForm,
    ClientUserUpdateForm,
    ClientUpdateForm,
)


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse("accounts:register-shelter")
        self.dummy_user = User.objects.create(
            username="peter7",
            email="peter@matchapet.com",
            first_name="Peter",
            last_name="Voltz",
            address="5th Ave",
            city="Manhattan",
            state="New York",
            zip_code="11209",
            password="test123abc",
        )

        self.user = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }
        self.user_no_username = {
            "username": "",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_name_exists = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_email_exists = {
            "username": "peter7",
            "email": "peter@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        self.user_hm_invalid_email = {
            "username": "peter7",
            "email": "pet@matchapet.com",
            "first_name": "Peter",
            "last_name": "Voltz",
            "address": "5th Ave",
            "city": "Manhattan",
            "state": "New York",
            "zip_code": "11209",
            "password1": "test123abc",
            "password2": "test123abc",
        }

        return super().setUp


class ShelterRegisterFormTest(BaseTest):
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


class UserRegisterFormTest(BaseTest):
    def test_form_not_valid(self):
        form = UserRegistrationForm(self.user_no_username)
        self.assertFalse(form.is_valid())

    def test_form_valid(self):
        form = UserRegistrationForm(self.user)
        self.assertFalse(form.is_valid())

    def test_form_username_exists(self):
        form = UserRegistrationForm(self.user_name_exists)
        form.has_error("username", "A user with that username already exists.")

    def test_form_email_exists(self):
        form = UserRegistrationForm(self.user_email_exists)
        form.has_error(
            "email",
            "This Email is already registered. "
            "Please use a different email address.",
        )

    def test_form_hm_invalid_email(self):
        form = UserRegistrationForm(self.user_hm_invalid_email)
        form.has_error(
            "This email is not a valid Email Address for Hiring Manager. "
            "Please use a different email address."
        )


# class BaseTest1(TestCase):
#     def setUp(self):
#         self.register_url = reverse("accounts:pet-register")
#         self.dummy_user = Pet.objects.create(
#             email="peter@matchapet.com",
#             pet_id="5",
#             pet_name="Sheila",
#             pet_breed="Dog",
#             pet_age="4",
#             pet_color="White",
#             pet_gender="Female",
#             date_entered="12/1/2020",
#         )

#         self.user = {
#             "pet_name": "Sheila",
#             "pet_breed": "Dog",
#             "pet_age": "4",
#             "pet_color": "White",
#             "pet_gender": "Female",
#             "date_entered": "12/1/2020",
#         }
#         self.user_no_username = {
#             "pet_name": "Sheila",
#             "pet_breed": "Dog",
#             "pet_age": "4",
#             "pet_color": "White",
#             "pet_gender": "Female",
#             "date_entered": "12/1/2020",
#         }

#         self.user_name_exists = {
#             "username": "peter7",
#             "email": "peter@matchapet.com",
#             "first_name": "Peter",
#             "last_name": "Voltz",
#             "shelter_city": "Manhattan",
#             "shelter_state": "New York",
#             "password1": "test123abc",
#             "password2": "test123abc",
#         }

#         self.user_email_exists = {
#             "username": "peter7",
#             "email": "peter@matchapet.com",
#             "first_name": "Peter",
#             "last_name": "Voltz",
#             "shelter_city": "Manhattan",
#             "shelter_state": "New York",
#             "password1": "test123abc",
#             "password2": "test123abc",
#         }

#         self.user_hm_invalid_email = {
#             "username": "peter7",
#             "email": "pet@matchapet.com",
#             "first_name": "Peter",
#             "last_name": "Voltz",
#             "shelter_city": "Manhattan",
#             "shelter_state": "New York",
#             "password1": "test123abc",
#             "password2": "test123abc",
#         }

#         return super().setUp
