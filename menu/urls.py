# menu/urls.py
from django.urls import path
from .views import menu, redirect_menu_html

urlpatterns = [
    path('', menu, name='menu'),  # Handle requests to /menu/
    path('about.html', redirect_menu_html, name='redirect_menu_html'), # Redirect from /menu.html to /menu/ 
]