# Generated by Django 3.2 on 2022-06-06 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]