from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path("", views.main_map, name="main-map"),
    url("maps/", views.default_map, name="sheltermaps"),
    url("maps/test/", views.map_test, name="maptest"),
]