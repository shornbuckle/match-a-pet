from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView
from django_tables2 import SingleTableView
import django_filters
from django_filters.views import FilterView
from .forms import ShelterRegistrationForm, ShelterUpdateForm, PetForm, PetListFormHelper
from .filters import PetFilter
from .models import Pet
from .tables import PetTable
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

global form

def home(request):
    return render(request, 'accounts/home.html')

def registerShelter(request):
    if request.method == 'POST':
         
        form = ShelterRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account succesfully created for {email} !')
            return redirect('/login/shelter')
    else:
        form = ShelterRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})

def registerUser(request):
    return HttpResponse("You are now at the User Regitration.")

def loginShelter(request):
    return render(request, 'accounts/login.html')

#def viewPets(request): (Sean 10/25 Testing Ways to Show Tables)
    #return render(request, 'accounts/view_pets.html', {'obj': Pet.objects.all()})

class PetListView(SingleTableView, FilterView): #method we will use to load tables into View Pets
    model = Pet
    table_class = PetTable
    template_name = 'accounts/view_pets.html'
    filterset_class = PetFilter
    formhelper_class = PetListFormHelper

def petsRegister(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.email = request.user
            instance.save()
            form.save()
            pet = form.cleaned_data.get('pet_name')
            messages.success(request, f'Pet profile created for {pet}!')
            return render(request, 'accounts/pets.html', {'form': form})

    else:
        form = PetForm()
    return render(request, 'accounts/pets.html', {'form': form})

@login_required
def shelterProfile(request):
    if request.method == 'POST':
        shelterUpdateForm = ShelterUpdateForm(request.POST, instance=request.user)
        if shelterUpdateForm.is_valid():
            shelterUpdateForm.save()
            messages.success(request, f'Account succesfully updated!')
            return redirect('/profile/shelter')
    else:
        shelterUpdateForm = ShelterUpdateForm(instance=request.user)

    context = {'shelterUpdateForm':shelterUpdateForm}

    return render(request, 'accounts/shelterProfile.html', context)





