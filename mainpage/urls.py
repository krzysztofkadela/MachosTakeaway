from django.urls import path
from .views import index  # Import your index view

urlpatterns = [
    path('', index, name='index'),  # Map the root URL to the index view
]