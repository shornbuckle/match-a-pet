from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShelterRegisterData, Pet

# Register your models here.

admin.site.site_header = "Math-A-Pet Admin Page"


class RegisterShelterAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "shelter_city",
        "shelter_state",
        "last_login",
        "is_active",
        "is_staff",
        "is_admin",
        "is_superuser",
    )
    search_fields = (
        "email",
        "username",
    )
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(ShelterRegisterData, RegisterShelterAdmin)


class PetRegisterAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "pet_name",
        "pet_breed",
        "pet_age",
        "pet_color",
        "pet_gender",
        "date_entered",
        "pet_id",
    )
    search_fields = (
        "pet_name",
        "pet_breed",
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Pet, PetRegisterAdmin)
