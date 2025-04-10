"""
URL configuration for takeaway project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', include('about.urls')),  # Include the about app URLs
    path('accounts/', include('allauth.urls')),  # Allauth account management
    path('menu/', include('menu.urls')),  # Include the menu app URLs
    path('', include('mainpage.urls')),  # Include the mainpage app URLs
    path('admin/', admin.site.urls),
    path('reservation/', include('reservation.urls')),  # Reservation URLs
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
