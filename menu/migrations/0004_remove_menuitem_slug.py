# Generated by Django 4.2.16 on 2024-11-23 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menuitem_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='slug',
        ),
    ]
