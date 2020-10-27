from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ShelterRegistrationForm, ShelterUpdateForm, PetForm
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

def petsRegister(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
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
        shelterUpdateForm = ShelterUpdateForm(request.POST, 
                            request.FILES, 
                            instance=request.user)
        if shelterUpdateForm.is_valid():
            shelterUpdateForm.save()
            messages.success(request, f'Account succesfully updated!')
            return redirect('/profile/shelter')
    else:
        shelterUpdateForm = ShelterUpdateForm(instance=request.user)

    context = {'shelterUpdateForm':shelterUpdateForm}

    return render(request, 'accounts/shelterProfile.html', context)





