from accounts.models import User
import json
from django.core import serializers

def users_to_geo():
    user = serializers.serialize('json',User.objects.all(), fields=('username','latitude','longitude')) #serialize into JSON file
    user_json=json.loads(user) # parse the user data


    length = len(user_json)
    current = user_json[0]  # access the first element - we will iterate this one
    fields = current['fields']  # access to get the geo fields
    username = fields['username']  # access the username
    latitude = fields['latitude']  # access the latitude element
    longitude = fields['longitude']  # access the longitude element

    finalGeo = []  # initialize
    i = 0  # iterator for while loop
    while i < length:
        current = user_json[i]  # access the first element - we will iterate this one
        fields = current['fields']  # access to get the geo fields
        username = fields['username']  # access the username
        latitude = fields['latitude']  # access the latitude element
        if latitude != "":
            latitude = float(latitude)
        longitude = fields['longitude']  # access the longitude element
        if longitude != "":
            longitude = float(longitude)

        #adderl is the template we will use to input our information from each user json

        adderl = {
            'type': 'Feature',
            'properties':
                {
                    'description': '<strong> Description </strong><p><a href="shelter profile link" target="_blank" title="Opens in a new window">SHELTER NAME</a></p>',
                    'icon': 'dog-park'},
            'geometry':
                {'type': 'Point', 'coordinates': [longitude, latitude]}
        }
        finalGeo.append(adderl) #here we are appending each formatted user json to the list
        i = i + 1 #increment the iterator

    return (finalGeo) # return finalGeo which will be passed to our HTMl maps file
