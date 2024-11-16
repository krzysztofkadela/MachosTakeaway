from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('burger', 'Burger'),
        ('pizza', 'Pizza'),
        ('pasta', 'Pasta'),
        ('fries', 'Fries'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = CloudinaryField('image', overwrite=True, resource_type='image') 

    def __str__(self):
        return self.title
