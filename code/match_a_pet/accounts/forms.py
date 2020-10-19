
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ShelterRegisterData

class ShelterRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Shelter Email'
        self.fields['username'].label = 'Shelter Name'
        self.fields['first_name'].label = 'Shelter Staff First Name'
        self.fields['last_name'].label = 'Shelter Staff Last Name'

    l_choices = (('New York','New York'), ('California','California'))
    ny_choices = (('Manhattan','Manhattan'), ('Brooklyn','Brooklyn'), ('Queens','Queens'), ('Staten Island','Staten Island'), ('Bronx','Bronx'))
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    shelter_city = forms.ChoiceField(choices = ny_choices)
    shelter_state = forms.ChoiceField(choices = l_choices)

    class Meta:
        model = ShelterRegisterData
        fields = ['username', 'email', 'first_name', 'last_name', 'shelter_city', 'shelter_state', 'password1', 'password2',]
        help_texts = {'username': ('Shelter name can contain Letters, digits and @/./+/-/_ only.')}

class ShelterUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Shelter Email'
        self.fields['username'].label = 'Shelter Name'
        self.fields['first_name'].label = 'Shelter Staff First Name'
        self.fields['last_name'].label = 'Shelter Staff Last Name'

    l_choices = (('New York','New York'), ('California','California'))
    ny_choices = (('Manhattan','Manhattan'), ('Brooklyn','Brooklyn'), ('Queens','Queens'), ('Staten Island','Staten Island'), ('Bronx','Bronx'))
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    shelter_city = forms.ChoiceField(choices = ny_choices)
    shelter_state = forms.ChoiceField(choices = l_choices)

    class Meta:
        model = ShelterRegisterData
        fields = ['username', 'email', 'first_name', 'last_name', 'shelter_city', 'shelter_state',]
        help_texts = {'username': ('Shelter name can contain Letters, digits and @/./+/-/_ only.')}