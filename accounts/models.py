from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# User has fields address, city, date_joined, email, first_name,
# groups, id, is_active, is_clientuser, is_shelter, is_staff, is_superuser,
# last_login, last_name, logentry, password, phone, sprofile, state,
# uprofile, user_permissions, username, zip_code


class User(AbstractUser):
    is_shelter = models.BooleanField("shelter status", default=False)
    is_clientuser = models.BooleanField("clientuser status", default=False)
    phone = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5, blank=True)


# ShelterRegisterData has fields pet, shelter_profile_image, user, user_id
class ShelterRegisterData(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="sprofile"
    )
    shelter_profile_image = models.ImageField(
        default="default.jpg", upload_to="shelter_profile_pics", blank=True
    )

    def __str__(self):
        return f"{self.user.username} Shelter Profile"

    def save(self, *args, **kwargs):
        super(ShelterRegisterData, self).save(*args, **kwargs)

        img = Image.open(self.shelter_profile_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.shelter_profile_image.path)


# UserRegisterData has fields user, user_id, user_profile_image
class UserRegisterData(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="uprofile"
    )
    user_profile_image = models.ImageField(
        default="default.jpg", upload_to="user_profile_pics", blank=True
    )

    def __str__(self):
        return f"{self.user.username} ClientUser Profile"

    def save(self, *args, **kwargs):
        super(UserRegisterData, self).save(*args, **kwargs)
        img = Image.open(self.user_profile_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.user_profile_image.path)


class Pet(models.Model):
    shelterRegisterData = models.ForeignKey(
        ShelterRegisterData, null=True, on_delete=models.CASCADE, related_name="pet"
    )
    pet_name = models.CharField(max_length=80)
    pet_breed = models.CharField(max_length=50)
    pet_age = models.CharField(max_length=10)
    pet_color = models.CharField(max_length=50)
    pet_gender = models.CharField(max_length=50)
    pet_profile_image1 = models.ImageField(
        default="default.jpg", upload_to="pet_profile_pics", blank=True
    )
    pet_image_url = models.URLField(
        max_length=250,
        blank=True,
        default="https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48212723/1/?bust=1592050579&width=450",
    )
    pet_profile_image2 = models.ImageField(
        default="default.jpg", upload_to="pet_profile_pics", blank=True
    )
    pet_profile_image3 = models.ImageField(
        default="default.jpg", upload_to="pet_profile_pics", blank=True
    )

    def __str__(self):
        return self.pet_name

    # the below method will captilize the fist letter of the below listed fields
    # when they are entered. This is important for the column sorting to work.
    def save(self, *args, **kwargs):
        for field_name in [
            "pet_name",
            "pet_breed",
            "pet_color",
            "pet_gender",
        ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Pet, self).save(*args, **kwargs)

        img = Image.open(self.pet_profile_image1.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pet_profile_image1.path)

        img = Image.open(self.pet_profile_image2.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pet_profile_image2.path)

        img = Image.open(self.pet_profile_image3.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pet_profile_image3.path)
