from django.db import models
from appointment.models import Appointment
from django.contrib.auth.models import User  # Import the User model

# Create your models here.

class Table(models.Model):
    TABLE_SIZE_CHOICES = [
        (2, '2 People'),
        (4, '4 People'),
        (6, '6 People'),
    ]
    
    size = models.IntegerField(choices=TABLE_SIZE_CHOICES)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Table for {self.size} people - {'Booked' if self.is_booked else 'Available'}"
    
class TableBooking(Appointment):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for Table {self.table.size} - {self.start_time} to {self.end_time}"
