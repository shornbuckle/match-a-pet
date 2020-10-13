from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ShelterRegistartionForm

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/home.html')

def registerShelter(request):
    if request.method == 'POST':
        form = ShelterRegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'accounts/login.html', {'form':form})
    else:
        form = ShelterRegistartionForm()
    return render(request, 'accounts/register.html', {'form':form})

def registerUser(request):
    return HttpResponse("You are now at the User Regitration.")

def loginShelter(request):
    return render(request, 'accounts/login.html')


