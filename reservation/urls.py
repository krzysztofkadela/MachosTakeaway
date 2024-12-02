from django.urls import path
from .views import make_reservation

urlpatterns = [
    path('make-reservation/', make_reservation, name='make_reservation'),
]