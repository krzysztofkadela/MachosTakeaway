from django.contrib import admin
from .models import MenuItem

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    search_fields = ('title', 'description')
    list_filter = ('category',)

admin.site.register(MenuItem, MenuItemAdmin)
