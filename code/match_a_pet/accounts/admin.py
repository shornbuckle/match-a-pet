from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShelterRegisterData

# Register your models here.

class RegisterShelterAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'shelter_city', 'shelter_state', 'last_login', 'is_active', 'is_staff', 'is_admin', 'is_superuser')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ShelterRegisterData, RegisterShelterAdmin)