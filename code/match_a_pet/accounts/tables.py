
import django_tables2 as tables
from .models import Pet

class PetTable(tables.Table):     #will utilize Django Tables2 for viewing.
    class Meta:
        model = Pet
        template_name = "django_tables2/bootstrap.html"
        fields = ("pet_name", "pet_gender", "pet_breed", "pet_age", "pet_color",)