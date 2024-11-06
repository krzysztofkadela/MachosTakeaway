from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.

class About(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(default=timezone.now)  # Automatically set on creation
    updated_on = models.DateTimeField(auto_now=True)  # Automatically set on update
    def __str__(self):
        return self.heading