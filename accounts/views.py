from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ShelterRegistrationForm, ShelterUpdateForm, PetForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import account_activation_token
from django.contrib.auth import get_user_model
from django.views import View
from django.http import HttpResponse
from django_tables2 import SingleTableView
from .models import Pet
from .tables import PetTable

global form


def home(request):
    return render(request, "accounts/home.html")


def registerShelter(request):
    if request.method == "POST":

        form = ShelterRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            current_site = get_current_site(request)
            email_subject = "Please activate your account on Match A Pet"
            email_body = {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
            }
            link = reverse(
                "accounts:activate",
                kwargs={"uidb64": email_body["uid"], "token": email_body["token"]},
            )
            activate_url = "http://" + current_site.domain + link

            send_mail(
                email_subject,
                "Hi "
                + first_name
                + " "
                + last_name
                + ", Please the link below to activate your account: \n"
                + activate_url,
                "nyu-match-a-pet@gmail.com",
                [email],
            )

            messages.success(
                request,
                "Account successfully created. Please check your email to verify your account.",
            )
            return redirect("/login/shelter")
    else:
        form = ShelterRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def registerUser(request):
    return HttpResponse("You are now at the User Registration.")

def petProfile(request):
    return render(request, "accounts/pet_profile.html")

def shelter_profile(request):
    return render(request, "accounts/shelter_profile.html")

def loginShelter(request):
    return render(request, "accounts/login.html")


class PetListView(SingleTableView):  # method we will use to load tables into View Pets
    model = Pet
    table_class = PetTable
    template_name = "accounts/view_pets.html"


def petsRegister(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.email = request.user
            instance.save()
            form.save()
            pet = form.cleaned_data.get("pet_name")
            messages.success(request, f"Pet profile created for {pet}!")
            return render(request, "accounts/pets.html", {"form": form})

    else:
        form = PetForm()
    return render(request, "accounts/pets.html", {"form": form})


@login_required
def shelterProfile(request):
    if request.method == "POST":
        shelterUpdateForm = ShelterUpdateForm(
            request.POST, request.FILES, instance=request.user
        )
        if shelterUpdateForm.is_valid():
            shelterUpdateForm.save()
            messages.success(request, "Account succesfully updated!")
            return redirect("/profile/shelter")
    else:
        shelterUpdateForm = ShelterUpdateForm(instance=request.user)

    context = {"shelterUpdateForm": shelterUpdateForm}

    return render(request, "accounts/shelterProfile.html", context)


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account successfully verified")
            return redirect("/login/shelter")
        else:
            messages.success(request, "Activation link is invalid")
            return redirect("/login/shelter")
