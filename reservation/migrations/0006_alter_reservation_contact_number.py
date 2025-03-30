# Generated by Django 4.2.16 on 2025-03-30 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_reservation_special_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='contact_number',
            field=models.CharField(help_text="Enter a valid phone number (9-15 digits, optional '+').", max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+999999999' (9 to 15 digits).", regex='^\\+?\\d{9,15}$')]),
        ),
    ]
