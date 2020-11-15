from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("maps/shelters/", views.map_func, name="map-shelters"),
    path("maps/test/", views.map_test, name="map-test"),
    path("maps/test2/", views.map_test2, name="map-test"),
]
