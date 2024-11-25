from django.db import models
from django.contrib.auth.models import User

# Table model
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
    
# TableBooking model
class TableBooking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # Link to User
    booking_time = models.DateTimeField(auto_now_add=True)  # Time of booking
    is_approved = models.BooleanField(default=False)  # Approval field for admin

    def __str__(self):
        return f"Booking for Table {self.table.size} by {self.user.username if self.user else 'Guest'} - Approved: {self.is_approved}"