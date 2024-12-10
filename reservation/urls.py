from django.urls import path
from .views import make_reservation, cancel_reservation # importing views

urlpatterns = [
    path('make-reservation/', make_reservation, name='make_reservation'),# make reservation URL
    path('cancel-reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),  # URL for cancelling reservation
]