from django import forms
from .models import Reservation, RestaurantSettings
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


class ReservationForm(forms.ModelForm):
    """
    Reservation form with validation to prevent booking for past dates
    and ensure booking is at least 24 hours in advance.
    """
    NUMBER_OF_GUESTS_CHOICES = [(i, str(i)) for i in range(1, 7)]

    number_of_guests = forms.ChoiceField(
        choices=NUMBER_OF_GUESTS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control nice-select wide',
            'required': 'required'
        })
    )

    booking_time = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={
            'class': 'form-control nice-select wide',
            'required': 'required'
        })
    )

    special_requests = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Special Requests (max 50 characters)',
            'maxlength': '50'
        })
    )

    class Meta:
        model = Reservation
        fields = [
            'number_of_guests',
            'contact_number',
            'booking_date',
            'booking_time',
            'special_requests'
        ]
        widgets = {
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number',
                'required': 'required'
            }),
            'booking_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': 'required'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate time slots from restaurant settings
        self.fields['booking_time'].choices = self.get_available_times()

    def get_available_times(self):
        """
        Generate time choices from opening to closing time.
        """
        settings = RestaurantSettings.objects.first()
        if not settings:
            return []
        available_times = []

        current_time = datetime.combine(
            datetime.today(), settings.opening_time
        )
        end_time = datetime.combine(
            datetime.today(), settings.closing_time
        )

        while current_time <= end_time:
            time_str = current_time.strftime("%H:%M")
            available_times.append((time_str, time_str))
            current_time += timedelta(hours=1)

        return available_times

    def clean(self):
        """
        Ensure the booking is at least 24 hours in advance.
        """
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        if booking_date and booking_time:
            full_datetime = datetime.combine(
                booking_date,
                datetime.strptime(booking_time, "%H:%M").time()
            )

            if full_datetime < datetime.now() + timedelta(hours=24):
                raise ValidationError(
                    'Reservations must be made at least 24 hours in advance.'
                )

        return cleaned_data
