# Generated by Django 3.2 on 2022-06-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes_available',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
