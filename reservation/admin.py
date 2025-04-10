from django.contrib import admin
from .models import Reservation, RestaurantSettings


# Reservation model for Django admin
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'booking_date', 'booking_time',
        'number_of_guests', 'is_approved'
    )
    list_filter = (
        'booking_date', 'number_of_guests', 'is_approved'
    )  # Filters for list view
    search_fields = (
        'user__username', 'contact_number'
    )  # Enable search by username or contact


# RestaurantSettings model for Django admin
@admin.register(RestaurantSettings)
class RestaurantSettingsAdmin(admin.ModelAdmin):
    list_display = ('opening_time', 'closing_time')