from django import forms
from .models import Reservation



class ReservationFormOldnoChoice_for_numquest(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['number_of_guests', 'contact_number', 'booking_date', 'booking_time']
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'number_of_guests': forms.Select(attrs={'class': 'form-control nice-select wide'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class ReservationForm(forms.ModelForm):
    NUMBER_OF_GUESTS_CHOICES = [(i, str(i)) for i in range(1, 7)]  # Creates a list of tuples (1, '1'), (2, '2'), ..., (6, '6')
    
    number_of_guests = forms.ChoiceField(choices=NUMBER_OF_GUESTS_CHOICES, widget=forms.Select(attrs={'class': 'form-control nice-select wide'}))

    class Meta:
        model = Reservation
        fields = ['number_of_guests', 'contact_number', 'booking_date', 'booking_time']
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }