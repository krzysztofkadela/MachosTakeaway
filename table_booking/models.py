from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
import datetime

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


class RestaurantSettings(models.Model):
    opening_time = models.TimeField(default=datetime.time(10, 0))  # Default to 10 AM
    closing_time = models.TimeField(default=datetime.time(22, 0))   # Default to 10 PM

    def __str__(self):
        return f"Restaurant Hours: {self.opening_time.strftime('%H:%M')} to {self.closing_time.strftime('%H:%M')}"


class TableBooking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # Link to User
    phone_number = models.CharField(max_length=15, default='Unknown')  # Field for user's phone number
    num_people = models.IntegerField(default=1)  # Field for number of people, st to 1 default
    booking_time = models.DateTimeField()  # Time of booking
    is_approved = models.BooleanField(default=False)  # Approval field for admin

    def clean(self):
        # Fetch the current restaurant settings
        settings = RestaurantSettings.objects.first()
        if not settings:
            raise ValidationError("No restaurant settings found. Please configure the settings.")

        # Check if the booking time is within 2 weeks
        if self.booking_time < timezone.now():
            raise ValidationError("Booking time cannot be in the past.")
        if self.booking_time > timezone.now() + timedelta(weeks=2):
            raise ValidationError("Booking can only be made up to 2 weeks in advance.")
        
        # check for people choice
        if not (1 <= self.num_people <= 6):
            raise ValidationError("Number of people must be between 1 and 6.")

        # Check if the table is already booked within the next 2 hours
        two_hours_later = self.booking_time + timedelta(hours=2)
        if TableBooking.objects.filter(table=self.table, booking_time__range=(self.booking_time, two_hours_later)).exists():
            raise ValidationError("This table is already booked during this time. Please choose a different time.")

        # Check if booking time is within operating hours
        if not (settings.opening_time <= self.booking_time.time() <= settings.closing_time):
            raise ValidationError(f"Bookings must be made between {settings.opening_time.strftime('%H:%M')} and {settings.closing_time.strftime('%H:%M')}.")

    def save(self, *args, **kwargs):
        # This will call the clean method before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for Table {self.table.size} by {self.user.username if self.user else 'Guest'} at {self.booking_time} - Approved: {self.is_approved}"