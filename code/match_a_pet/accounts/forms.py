
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.db import models
from django import forms

#reference : https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/

class ShelterRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Shelter Email'
        self.fields['username'].label = 'Shelter Name'
        self.fields['first_name'].label = 'Shelter Staff First Name'
        self.fields['last_name'].label = 'Shelter Staff Last Name'

    l_choices = (('1','New York'), ('2','California'))
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    shelter_state = forms.ChoiceField(choices = l_choices)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'shelter_state', 'password1', 'password2',]
        help_texts = {'username': ('Shelter name can contain Letters, digits and @/./+/-/_ only.')}


class PetForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet_name'].label = 'Pet Name'
        self.fields['pet_breed'].label = 'Pet Breed'
        self.fields['pet_age'].label = 'Pet Age'
        self.fields['pet_color'].label = 'Pet Color'
        self.fields['shelter_id'].label = 'Shelter Id'
        self.fields['date_entered'].label = 'Date Entered'

    pet_name = forms.CharField(required = True)
    pet_breed = forms.CharField(required = True)
    pet_age = forms.CharField(required=True)
    pet_color = forms.CharField(required=True)
    shelter_id = forms.CharField(required=True)
    date_entered = forms.CharField(required=True)

