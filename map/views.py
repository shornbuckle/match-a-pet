from django.shortcuts import render
import requests
from django.core import serializers
from accounts.models import User

#Google API KEY AIzaSyC796wfP4gXyVbNt2wpSW6zMUojqenu04w

mapbox_access_token = 'pk.eyJ1Ijoic2hvcm5idWNrbGU5MyIsImEiOiJja2g5b3QxZnEwM3V3MnprM3gxZzlnMTlnIn0.U0IY_rRntdyeFAnW7bCSIQ'
def default_map(request):
    return render(request, 'map/sheltermaps.html', {'mapbox_access_token': mapbox_access_token })

def map_shelter(request):

    #user = serializers.serialize( "python", User.objects.all() )
    user = User.objects.all()
    return render(
        request,
        'map/test.html',
        {
            'mapbox_access_token': mapbox_access_token,
            'user': user,
        })

def map_shelter2(request):

    #user = serializers.serialize( "python", User.objects.all() )
    user = User.objects.all()
    return render(
        request,
        'map/test_scratch_work.html',
        {
            'mapbox_access_token': mapbox_access_token,
            'user': user,
        })

