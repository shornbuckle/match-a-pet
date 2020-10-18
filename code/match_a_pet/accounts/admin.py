from django.contrib import admin
from .models import ShelterRegisterData
from .models import Pet

# Register your models here.
admin.site.register(ShelterRegisterData)
admin.site.register(Pet)