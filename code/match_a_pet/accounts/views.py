from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the Home.")

def registerShelter(request):
    return HttpResponse("You are now at the Shelter Regitration.")

def registerUser(request):
    return HttpResponse("You are now at the User Regitration.")
