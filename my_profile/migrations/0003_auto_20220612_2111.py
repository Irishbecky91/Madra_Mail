# Generated by Django 3.2 on 2022-06-12 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_auto_20220612_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_country',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_county',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_phone_number',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_postcode',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_street_address1',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_street_address2',
        ),
        migrations.RemoveField(
            model_name='usersprofile',
            name='default_town_or_city',
        ),
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=254)),
                ('breed', models.CharField(blank=True, max_length=100, null=True)),
                ('measurement_a', models.IntegerField()),
                ('measurement_b', models.IntegerField()),
                ('measurement_c', models.IntegerField()),
                ('pet_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.usersprofile')),
            ],
        ),
    ]
