from django.contrib import admin
from .models import ShelterRegisterData, Pet, UserRegisterData, User
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = "Math-A-Pet Admin Page"


class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "city",
        "state",
        "last_login",
        "is_active",
        "is_shelter",
        "is_clientuser",
        "is_staff",
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


class ClientUserModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "user_id",
        "user_profile_image",
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# admin.site.register(ShelterRegisterData, RegisterShelterAdmin)
admin.site.register(User, UserModelAdmin)
admin.site.register(UserRegisterData, ClientUserModelAdmin)


@admin.register(Pet, ShelterRegisterData)
class ViewAdmin(ImportExportModelAdmin):
    pass
    # list_display = (
    #     # "email",
    #     "pet_name",
    #     "pet_breed",
    #     "pet_age",
    #     "pet_color",
    #     "pet_gender",
    #     # "date_entered",
    # )
    # search_fields = (
    #     "pet_name",
    #     "pet_breed",
    # )

    # filter_horizontal = ()
    # list_filter = ()
    # fieldsets = ()


# admin.site.register(Pet, PetRegisterAdmin)
