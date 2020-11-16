from django.urls import path
from django.conf.urls import url
from . import views

app_name = "playdate"
urlpatterns = [
    path("playdate/test/", views.playdate_test, name="play-date"),
    path("user/petregister/", views.clientUserPetsRegister, name="user-pet-register"),
]
