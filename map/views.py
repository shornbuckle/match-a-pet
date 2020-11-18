from django.shortcuts import render
import requests
from django.core import serializers
from accounts.models import User
from map.helpers import users_to_geo

# Google API KEY AIzaSyC796wfP4gXyVbNt2wpSW6zMUojqenu04w

mapbox_access_token = "pk.eyJ1Ijoic2hvcm5idWNrbGU5MyIsImEiOiJja2g5b3QxZnEwM3V3MnprM3gxZzlnMTlnIn0.U0IY_rRntdyeFAnW7bCSIQ"
#final_geo = users_to_geo()
#final_geo = "".join(str(x) for x in final_geo)

def map_func(request):
    user = User.objects.all()
    print(user[450].longitude)
    # return render(
    #     request,
    #     'map/maps-shelters.html',
    #     {
    #         'mapbox_access_token': mapbox_access_token,
    #         'user': user,
    #     })

    context = {
    'mapbox_access_token': mapbox_access_token,
    'user': user,
    }
    return render(request, 'map/maps-shelters.html', context)


def map_test(request):

    #user = serializers.serialize( "python", User.objects.all() )
    #user = User.objects.all()
    return render(
        request,
        'map/map-test.html',
        {
            'mapbox_access_token': mapbox_access_token,
            'final_geo': final_geo
        })

def map_test2(request):

    #user = serializers.serialize( "python", User.objects.all() )
    user = User.objects.all()
    return render(
        request,
        'map/map-test2.html',
        {
            'mapbox_access_token': mapbox_access_token,
            'user': user,
        })

