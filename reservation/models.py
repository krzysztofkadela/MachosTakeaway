from django.db import models

# Create your models here.
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    reservation_date = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    number_of_guests = models.PositiveIntegerField() 
    contact_number = models.CharField(max_length=15)
    booking_date = models.DateField()  # Field for the date of booking
    booking_time = models.TimeField()   # Field for the time of booking

    def __str__(self):
        return f'Reservation for {self.customer_name} on {self.booking_date} at {self.booking_time}'