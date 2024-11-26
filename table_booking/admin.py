from django.contrib import admin
from .models import Table, TableBooking, RestaurantSettings

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('size', 'is_booked')

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('table', 'user', 'booking_time', 'is_approved')

@admin.register(RestaurantSettings)
class RestaurantSettingsAdmin(admin.ModelAdmin):
    list_display = ('opening_time', 'closing_time')