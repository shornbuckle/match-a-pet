
import django_filters
from .models import Pet

class PetFilter(django_filters.FilterSet):
    pet_gender = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Pet
        fields = ['pet_gender',]