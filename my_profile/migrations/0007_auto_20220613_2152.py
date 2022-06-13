# Generated by Django 3.2 on 2022-06-13 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_profile', '0006_rename_pet_petprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petprofile',
            old_name='user',
            new_name='pet_owner',
        ),
        migrations.AlterField(
            model_name='petprofile',
            name='measurement_a',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='petprofile',
            name='measurement_b',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='petprofile',
            name='measurement_c',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
