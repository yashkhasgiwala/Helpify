# Generated by Django 3.1.3 on 2020-11-21 12:48

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201121_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
