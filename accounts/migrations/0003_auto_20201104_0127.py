# Generated by Django 3.1.2 on 2020-11-04 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20201104_0046"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="email",
        ),
        migrations.AlterField(
            model_name="pet",
            name="id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]