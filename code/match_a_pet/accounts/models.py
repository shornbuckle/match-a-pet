from django.db import models


class ShelterRegisterData(models.Model):
    shelter_id = models.AutoField(primary_key=True)
    shelter_email = models.EmailField(max_length = 254, unique = True)
    shelter_name = models.CharField(max_length=80)
    shelter_address = models.CharField(max_length=200)
    shelter_city = models.CharField(max_length=50)
    shelter_state = models.CharField(max_length=50)

    def __str__(self):
        return self.shelter_email