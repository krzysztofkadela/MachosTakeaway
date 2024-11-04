from django.db import models

# Create your models here.

class About(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.heading