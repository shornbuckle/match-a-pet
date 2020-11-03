# Generated by Django 3.1.2 on 2020-10-28 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShelterRegisterData',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('shelter_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('shelter_city', models.CharField(max_length=50)),
                ('shelter_state', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('shelter_profile_image', models.ImageField(blank=True, default='default.jpg', upload_to='shelter_profile_pics')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('pet_id', models.AutoField(primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=80)),
                ('pet_breed', models.CharField(max_length=50)),
                ('pet_age', models.CharField(max_length=3)),
                ('pet_color', models.CharField(max_length=50)),
                ('pet_gender', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=50)),
                ('pet_profile_image1', models.ImageField(blank=True, default='default.jpg', upload_to='pet_profile_pics')),
                ('pet_profile_image2', models.ImageField(blank=True, default='default.jpg', upload_to='pet_profile_pics')),
                ('pet_profile_image3', models.ImageField(blank=True, default='default.jpg', upload_to='pet_profile_pics')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
