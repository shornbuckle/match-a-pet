
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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