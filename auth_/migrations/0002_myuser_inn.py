# Generated by Django 4.0.5 on 2022-06-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='INN',
            field=models.IntegerField(null=True, unique=True, verbose_name='Identification number'),
        ),
    ]
