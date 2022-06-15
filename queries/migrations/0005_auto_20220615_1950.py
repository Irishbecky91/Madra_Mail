# Generated by Django 3.2 on 2022-06-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0004_alter_query_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='username',
        ),
        migrations.AlterField(
            model_name='query',
            name='query_type',
            field=models.CharField(choices=[('QUERY', 'Ask A Question'), ('QUOTE', 'Request A Quote')], max_length=20),
        ),
    ]
