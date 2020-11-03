from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def home(request):
    return render(request, "accounts/home.html")


class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_ShelterUser:
            return render(request, 'accounts/shelter_home.html')
        else:
            return render(request, 'accounts/user_home.html')
    return render(request, 'accounts/home.html')