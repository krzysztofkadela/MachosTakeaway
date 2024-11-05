from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here

class CustomerComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the User model
    comment = models.TextField()                               # Comment text
    comment_date = models.DateTimeField(default=timezone.now) # Date of comment
    updated_on = models.DateTimeField(auto_now=True)         # Automatically set to now when the comment is updated
    is_approved = models.BooleanField(default=False)          # Approval status of the comment

    def __str__(self):
        return f"{self.user.username} - {self.comment[:20]}"  # Display user's username and first 20 characters of the comment