from django.urls import path
from .views import index, add_comment # Import your index view
from .views import custom_login, custom_logout, user_comments #search_view

urlpatterns = [
    path('', index, name='index'),  # Map the root URL to the index view
    path('add_comment/', add_comment, name='add_comment'),
    path('user_comments/', user_comments, name='user_comments'),
    path('login/', custom_login, name='login'),  # Ensure this path exists
    path('logout/', custom_logout, name='logout'),
]