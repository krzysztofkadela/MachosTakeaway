from django import forms
from .models import Reservation

class ReservationFormon(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'number_of_guests', 'contact_number', 'booking_date', 'booking_time']
        widgets = {
            'booking_date': forms.SelectDateWidget(),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'number_of_guests', 'contact_number', 'booking_date', 'booking_time']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'number_of_guests': forms.Select(attrs={'class': 'form-control nice-select wide'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }