from django import forms
from .models import Reservation, RestaurantSettings
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

# Form with required in fields.
class ReservationForm(forms.ModelForm):
    NUMBER_OF_GUESTS_CHOICES = [(i, str(i)) for i in range(1, 7)]
    number_of_guests = forms.ChoiceField(choices=NUMBER_OF_GUESTS_CHOICES, 
                                          widget=forms.Select(attrs={'class': 'form-control nice-select wide', 'required': 'required'}))

    booking_time = forms.ChoiceField(choices=[], 
                                      widget=forms.Select(attrs={'class': 'form-control nice-select wide', 'required': 'required'}))

    special_requests = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                      'placeholder': 'Special Requests (max 50 characters)', 
                                      'maxlength': '50'})
    )

    class Meta:
        model = Reservation
        fields = ['number_of_guests', 'contact_number', 'booking_date', 'booking_time', 'special_requests']
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 
                                                      'placeholder': 'Your Phone Number', 
                                                      'required': 'required'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate the booking_time choices based on restaurant settings
        self.fields['booking_time'].choices = self.get_available_times()
    
    def get_available_times(self):
        """Generate available booking times based on restaurant settings."""
        settings = RestaurantSettings.objects.first()
        if not settings:
            return []  # No settings available
        available_times = []
        
        # Create time slots from opening time to closing time
        current_time = datetime.combine(datetime.today(), settings.opening_time)
        end_time = datetime.combine(datetime.today(), settings.closing_time)

        while current_time <= end_time:
            available_times.append((current_time.strftime("%H:%M"), current_time.strftime("%H:%M")))
            current_time += timedelta(hours=1)  # Increment by 1 hour
        
        return available_times

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        # Additional validation can be added here if needed
        return booking_time