#initiate

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
#from .forms import ShelterRegistrationForm, ShelterUpdateForm, PetForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from ..utils import account_activation_token
from django.contrib.auth import get_user_model
from django.views import View
from django.http import HttpResponse

global form

from django.contrib.auth import login
#from django.shortcuts import redirect
from django.views.generic import CreateView

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ..forms import ClientUserSignUpForm, ShelterUserSignUpForm
from ..models import User


class ShelterSignUpView(CreateView):
    model = User
    form_class = ShelterUserSignUpForm
    template_name = 'accounts/registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ShelterUser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/login/shelter")