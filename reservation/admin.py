from django.contrib import admin
from .models import Reservation, RestaurantSettings

# Register your models here.

# Reservation model for Django admin
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_date', 'booking_time', 'number_of_guests', 'is_approved')  # Fields to display in the admin list view
    list_filter = ('booking_date', 'number_of_guests', 'is_approved')  # Filters to apply in the list view
    search_fields = ('user__username', 'contact_number')  # Fields to provide search functionality

# RestaurantSettings model for Django admin
@admin.register(RestaurantSettings)
class RestaurantSettingsAdmin(admin.ModelAdmin):
    list_display = ('opening_time', 'closing_time')  # Fields to display in the admin list view