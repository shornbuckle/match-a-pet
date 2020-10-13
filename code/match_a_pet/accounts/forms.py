from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ShelterRegistartionForm(UserCreationForm):
    shelter_email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'shelter_email', 'password1', 'password2']