from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  # Import ValidationError

# Create your models here.

# Model to store all data for customer table reservation.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user model
    reservation_date = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    number_of_guests = models.PositiveIntegerField() 
    contact_number = models.CharField(max_length=15)
    booking_date = models.DateField()  # Field for the date of booking
    booking_time = models.TimeField()   # Field for the time of booking
    is_approved = models.BooleanField(default=False)  # Field to mark approval status
    special_requests = models.CharField(max_length=50, blank=True)  # Field for special requests

    def __str__(self):
        return f'Reservation for {self.user.username} on {self.booking_date} at {self.booking_time}'
    

# setiings for restaurant opening hours.
class RestaurantSettings(models.Model):
    opening_time = models.TimeField()  # Opening time
    closing_time = models.TimeField()  # Closing time 

    def clean(self):
        """Ensure that the opening time is before the closing time."""
        if self.opening_time >= self.closing_time:
            raise ValidationError('Closing time must be after opening time.')

    def __str__(self):
        return f"Open from {self.opening_time.strftime('%H:%M')} to {self.closing_time.strftime('%H:%M')}"