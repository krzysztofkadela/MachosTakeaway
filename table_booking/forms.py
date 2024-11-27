from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['table', 'phone_number', 'num_people', 'booking_time']  # Include necessary fields

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extract user from kwargs
        super().__init__(*args, **kwargs)  # Call the parent constructor
        if user:
            self.instance.user = user  # Automatically assign the user if provided