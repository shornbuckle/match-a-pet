import datetime

from django.db import models
from django.utils import timezone

class Shelter(models.Model):
    shelter_name = models.CharField(max_length=200, unique=True)



    def __str__(self):
        return self.shelter_name_text


