from django.db import models
from django.utils.text import slugify  # imports slug field
from cloudinary.models import CloudinaryField

# Create your models here.


# Menu items model with category.
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
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.description[:20])
            # Generate slug from first 30 characters of description
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
