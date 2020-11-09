from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path("", views.main_map, name="main-map"),
    path("maps/", views.default_map, name="sheltermaps"),
    path("maps/test/", views.map_test, name="maptest"),
]