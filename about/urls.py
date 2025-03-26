# about/urls.py
from django.urls import path
from .views import about_view, redirect_about_html

urlpatterns = [
    path('about/', about_view, name='about'),  # This should match the redirect
    path('about/redirect/', redirect_about_html, name='redirect_about'),
]