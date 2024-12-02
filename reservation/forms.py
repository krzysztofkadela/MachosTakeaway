from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'number_of_guests', 'contact_number', 'booking_date', 'booking_time']
        widgets = {
            'booking_date': forms.SelectDateWidget(),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }