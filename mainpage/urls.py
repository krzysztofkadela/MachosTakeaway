from django.urls import path
from .views import index  # Import your index view
from .views import custom_login, custom_logout, search_view

urlpatterns = [
    path('', index, name='index'),  # Map the root URL to the index view
    path('login/', custom_login, name='login'),  # Ensure this path exists
    path('logout/', custom_logout, name='logout'),
     path('search/', search_view, name='search'),  # Your search URL pattern
]