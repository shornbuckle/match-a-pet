from django.shortcuts import render
import requests

#Google API KEY AIzaSyC796wfP4gXyVbNt2wpSW6zMUojqenu04w

mapbox_access_token = 'pk.eyJ1Ijoic2hvcm5idWNrbGU5MyIsImEiOiJja2g5b3QxZnEwM3V3MnprM3gxZzlnMTlnIn0.U0IY_rRntdyeFAnW7bCSIQ'
def default_map(request):
    return render(request, 'map/sheltermaps.html', {'mapbox_access_token': mapbox_access_token })

def map_test(request):
    return render(request, 'map/test.html', {'mapbox_access_token': mapbox_access_token })

