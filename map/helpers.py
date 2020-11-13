from accounts.models import User
import json
from django.core import serializers

"""
finalGeo = []
user = User.objects.all()
for u in user:
    adderl = {
        'type': 'Feature',
        'properties':
            {
                'description': '<strong> Description </strong><p><a href="shelter profile link" target="_blank" title="Opens in a new window">SHELTER NAME</a></p>',
                'icon': 'dog-park'},
        'geometry':
            {'type': 'Point', 'coordinates': [u.longitude, u.lattitude]}
    }
    adderJ = json.dumps(adderl)
    finalGeo.append(adderJ)

print(finalGeo)
"""
User.objects.get(id=14).longitude

user = serializers.serialize("xml",User.objects.all())

finalGeo = []

adderl = {
    'type': 'Feature',
    'properties':
         {
            'description': '<strong> Description </strong><p><a href="shelter profile link" target="_blank" title="Opens in a new window">SHELTER NAME</a></p>',
            'icon': 'dog-park'},
     'geometry':
        {'type': 'Point', 'coordinates': [User.objects.get(id=14).longitude, User.objects.get(id=14).longitude]}
}
adderJ = json.dumps(adderl)
finalGeo.append(adderJ)

print(finalGeo)