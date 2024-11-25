from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['table', 'user']  # Include additional fields you want to capture
        widgets = {
            'user': forms.HiddenInput()  # Set user field to not be directly input by the user
        }