from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Regex for validating phone numbers
phone_regex = RegexValidator(
    regex=r'^\+?\d{9,15}$',
    message=(
        "Phone number must be entered in the format '+999999999' "
        "(9 to 15 digits)."
    )
)


class Reservation(models.Model):
    """
    Model to store all data for customer table reservation.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    reservation_date = models.DateTimeField(auto_now_add=True)
    number_of_guests = models.PositiveIntegerField()
    contact_number = models.CharField(
        max_length=15,
        validators=[phone_regex],
        help_text=(
            "Enter a valid phone number (9-15 digits, optional '+')."
        )
    )
    booking_date = models.DateField()
    booking_time = models.TimeField()
    is_approved = models.BooleanField(default=False)
    special_requests = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return (
            f'Reservation for {self.user.username} on '
            f'{self.booking_date} at {self.booking_time}'
        )


class RestaurantSettings(models.Model):
    """
    Settings for restaurant opening hours.
    """
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def clean(self):
        """
        Ensure that the opening time is before the closing time.
        """
        if self.opening_time >= self.closing_time:
            raise ValidationError(
                'Closing time must be after opening time.'
            )

    def __str__(self):
        return (
            f"Open from {self.opening_time.strftime('%H:%M')} to "
            f"{self.closing_time.strftime('%H:%M')}"
        )
