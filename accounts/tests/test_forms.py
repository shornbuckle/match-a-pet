from django.test import SimpleTestCase, TestCase
from accounts.forms import ShelterRegistrationForm, ShelterUpdateForm, PetForm


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

    def test_ShelterRegistrationForm_invalid_data1(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
                "shelter_city": "Manhattan",
                "shelter_state": "New York",
                "password1": "test123abc",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_ShelterRegistrationForm_invalid_data2(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
                "shelter_city": "Manhattan",
                "shelter_state": "New York",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_ShelterRegistrationForm_invalid_data3(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
                "shelter_city": "Manhattan",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_ShelterRegistrationForm_invalid_data4(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_ShelterRegistrationForm_invalid_data5(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_ShelterRegistrationForm_invalid_data6(self):
        form = ShelterRegistrationForm(
            data={
                "username": "peter7",
                "email": "peter@matchapet.com",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_ShelterRegistrationForm_invalid_data7(self):
        form = ShelterRegistrationForm(
            data={
                "email": "peter@matchapet.com",
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

    def test_ShelterUpdateForm_invalid_data1(self):
        form = ShelterUpdateForm(
            data={
                "username": "peter3",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_ShelterUpdateForm_valid2(self):
        form = ShelterUpdateForm(
            data={
                "username": "peter3",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_ShelterUpdateForm_valid3(self):
        form = ShelterUpdateForm(
            data={
                "username": "peter3",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
                "shelter_city": "Brooklyn",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_ShelterUpdateForm_valid4(self):
        form = ShelterUpdateForm(
            data={
                "username": "peter3",
                "email": "peter@matchapet.com",
                "first_name": "Peter",
                "last_name": "Voltz",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class TestForms(SimpleTestCase):
    def test_PetForm_valid(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
                "pet_breed": "Dog",
                "pet_age": "Baby",
                "pet_color": "White",
                "pet_gender": "Female",
                # "date_entered": "12/1/2020",
            }
        )

        self.assertTrue(form.is_valid())

    def test_PetForm_no_data(self):
        form = PetForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

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
        self.assertEquals(len(form.errors), 3)

    def test_PetForm_invalid_data4(self):
        form = PetForm(
            data={
                "pet_name": "Sheila",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


# ******
