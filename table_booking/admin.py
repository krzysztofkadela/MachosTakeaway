from django.contrib import admin


# admin.py
from django.contrib import admin
from .models import Table, TableBooking

class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('table', 'user', 'is_approved')  
    list_filter = ('is_approved',)
    search_fields = ('user__username', 'table__size')

admin.site.register(Table)
admin.site.register(TableBooking, TableBookingAdmin)