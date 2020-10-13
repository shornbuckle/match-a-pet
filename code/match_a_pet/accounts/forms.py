
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ShelterRegistrationForm(UserCreationForm):
    l_choices = (('1','New York'), ('2','California'))
    shelter_email = forms.EmailField()
    shelter_state = forms.ChoiceField(choices = l_choices)

    class Meta:
        model = User
        fields = ['username', 'shelter_email', 'shelter_state', 'password1', 'password2']