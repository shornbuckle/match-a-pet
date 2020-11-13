#from accounts.models import User
import json
from django.core import serializers

#user = serializers.serialize('json',User.objects.all(), fields=('username','latitude','longitude')) #serialize into JSON file
#y=json.loads(user) # parse the user data

testJson =[{'model': 'accounts.user', 'pk': 475, 'fields': {'username': 'benji', 'latitude': '40.6353593', 'longitude': '-74.0217069'}},
{'model': 'accounts.user', 'pk': 476, 'fields': {'username': 'Adam', 'latitude': '40.628065', 'longitude': '-74.019221'}}]



length = len(testJson)
current = testJson[0] #access the first element - we will iterate this one
fields = current['fields'] #access to get the geo fields
username = fields['username'] #access the username
latitude = fields['latitude'] #access the latitude element
longitude = fields['longitude'] #access the longitude element

print(length)
print(username)

finalGeo = {} #initialize

i = 0 #iterator for while loop
while i < length:
    current = testJson[i]  # access the first element - we will iterate this one
    fields = current['fields']  # access to get the geo fields
    username = fields['username']  # access the username
    latitude = fields['latitude']  # access the latitude element
    longitude = fields['longitude']  # access the longitude element


    adderl = {
        'type': 'Feature',
        'properties':
            {
                'description': '<strong> Description </strong><p><a href="shelter profile link" target="_blank" title="Opens in a new window">SHELTER NAME</a></p>',
                'icon': 'dog-park'},
        'geometry':
            {'type': 'Point', 'coordinates': [longitude, latitude]}
    }
    finalGeo.update(adderl)
    print(adderl)
    i = i + 1

print(finalGeo)
