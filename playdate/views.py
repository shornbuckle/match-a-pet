from django.shortcuts import render
import requests
from accounts.models import User
from django.contrib import messages
from map.helpers import users_to_geo
from .forms import ClientUserPetForm
from accounts.models import UserRegisterData


def playdate_test(request):

    user = User.objects.all()
    return render(
        request,
        'map/map-test2.html',
        {
            'user': user,
        })


def clientUserPetsRegister(request):
    if request.method == "POST":
        form = ClientUserPetForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userRegisterData = request.user.uprofile
            instance.save()
            form.save()
            pet = form.cleaned_data.get("pet_name")
            messages.success(request, f"Pet profile created for {pet}!")
            return render(request, "playdate/petRegister.html", {"form": form})

    else:
        form = ClientUserPetForm()
    return render(request, "playdate/petRegister.html", {"form": form})
