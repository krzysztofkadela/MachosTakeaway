from django.urls import path
from django.views.generic import TemplateView  # Import TemplateView for success page
from .views import book_table  # Importing your view

urlpatterns = [
    path('book/', book_table, name='book_table'),  # URL path for booking a table
    path('booking_success/', TemplateView.as_view(template_name='booking_success.html'), name='booking_success'),  # Success page
]