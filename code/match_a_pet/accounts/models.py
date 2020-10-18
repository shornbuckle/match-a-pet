from django.db import models
from django.forms import ModelForm

class ShelterRegisterData(models.Model):
    shelter_id = models.AutoField(primary_key=True)
    shelter_email = models.EmailField(max_length = 254, unique = True)
    shelter_name = models.CharField(max_length=80)
    shelter_address = models.CharField(max_length=200)
    shelter_city = models.CharField(max_length=50)
    shelter_state = models.CharField(max_length=50)

    def __str__(self):
        return self.shelter_email



class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=80)
    pet_breed = models.CharField(max_length=50)
    pet_age = models.CharField(max_length=3)
    pet_color = models.CharField(max_length=50)
    pet_gender = models.CharField(max_length=50)
    shelter_id = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=50)

    def __str__(self):
        return self.pet_name

#class PetForm(ModelForm):
#    class Meta:
#        model = Pet
 #       fields = ['pet_id', 'pet_name', 'pet_breed', 'pet_age', 'pet_color','pet_gender', 'shelter_id', 'date_entered']