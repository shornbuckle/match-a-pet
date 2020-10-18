from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ShelterRegistrationForm, PetForm

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/home.html')

def registerShelter(request):
    if request.method == 'POST':
        form = ShelterRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('shelter_name')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'accounts/login.html', {'form':form})
    else:
        form = ShelterRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})

def registerUser(request):
    return HttpResponse("You are now at the User Regitration.")

def loginShelter(request):
    return render(request, 'accounts/login.html')

def petsRegister(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            pet = form.cleaned_data.get('pet_name')
            messages.success(request, f'Pet profile created for {pet}!')
            return render(request, 'accounts/pets.html', {'form': form})

    else:
        form = PetForm()
    return render(request, 'accounts/pets.html', {'form': form})


