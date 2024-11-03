# about/urls.py
from django.urls import path
from .views import about, redirect_about_html

urlpatterns = [
    path('', about, name='about'), #respond to /about/ 
    path('about.html', redirect_about_html, name='redirect_about_html'), # Redirect from /about.html to /about/ 
]