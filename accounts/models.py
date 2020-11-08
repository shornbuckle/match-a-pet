from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# from django.forms import ModelForm
from PIL import Image


class MyAccountManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        first_name,
        last_name,
        shelter_city,
        shelter_state,
        password=None,
    ):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have a First Name")
        if not last_name:
            raise ValueError("Users must have a Last Name")
        if not shelter_city:
            raise ValueError("Shelters must provide a Shelter City")
        if not shelter_state:
            raise ValueError("Shelters must provide a Shelter State")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            shelter_city=shelter_city,
            shelter_state=shelter_state,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        username,
        first_name,
        last_name,
        shelter_city,
        shelter_state,
        password=None,
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            shelter_city=shelter_city,
            shelter_state=shelter_state,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ShelterRegisterData(AbstractBaseUser):

    # l_choices = (('1','New York'), ('2','California'))

    # shelter_id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30)
    # shelter_name = models.CharField(max_length=80)
    # shelter_address = models.CharField(max_length=200)
    shelter_city = models.CharField(max_length=50)
    shelter_state = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shelter_profile_image = models.ImageField(
        default="default.jpg", upload_to="shelter_profile_pics", blank=True
    )
    # shelter_state = models.ChoiceField(choices = l_choices)

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "shelter_city",
        "shelter_state",
    ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # def save(self):
    #     super().save()

    #     img = Image.open(self.shelter_profile_image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.shelter_profile_image.path)


class Pet(models.Model):
    # email = models.ForeignKey(ShelterRegisterData, on_delete=models.CASCADE, primary_key=True)
    id = models.ForeignKey(
        ShelterRegisterData, on_delete=models.CASCADE, primary_key=True
    )
    # shelter_id = models.ForeignKey(ShelterRegisterData, on_delete=models.CASCADE)
    #pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=80)
    pet_breed = models.CharField(max_length=50)
    pet_age = models.CharField(max_length=10)
    pet_color = models.CharField(max_length=50)
    pet_gender = models.CharField(max_length=50)
    # date_entered = models.CharField(max_length=50)
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
