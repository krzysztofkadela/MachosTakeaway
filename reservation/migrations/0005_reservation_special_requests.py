# Generated by Django 4.2.16 on 2024-12-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_restaurantsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='special_requests',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
