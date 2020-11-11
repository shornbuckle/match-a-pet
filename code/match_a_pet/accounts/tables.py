import django_tables2 as tables
from .models import Pet


class PetTable(tables.Table):  # will utilize Django Tables2 for viewing.

<<<<<<< HEAD
    pet_image_url = tables.Column(verbose_name="Profile Picture")
    pet_image_url = tables.TemplateColumn(
        '<img src="{{record.pet_image_url}}" style="width:300px; height:300px"> '
    )
=======
>>>>>>> main
    pet_name = tables.Column(verbose_name="Name")
    pet_gender = tables.Column(verbose_name="Gender")
    pet_breed = tables.Column(verbose_name="Breed")
    pet_age = tables.Column(verbose_name="Age")
    pet_color = tables.Column(verbose_name="Color")

    class Meta:
        model = Pet
        template_name = "django_tables2/bootstrap.html"
        fields = (
<<<<<<< HEAD
            "pet_image_url",
=======
>>>>>>> main
            "pet_name",
            "pet_gender",
            "pet_breed",
            "pet_age",
            "pet_color",
        )
