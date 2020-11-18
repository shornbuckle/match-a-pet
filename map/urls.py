from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("maps/shelters/", views.map_func, name="map-shelters"),
]