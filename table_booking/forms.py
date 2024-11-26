from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['table', 'phone_number', 'num_people', 'booking_time']  # Include necessary fields

    num_people = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 7)],  # Choices from 1 to 6
        initial=1,  # Set default to 1
    )