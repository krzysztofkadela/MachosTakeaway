from django.urls import path
from .views import make_reservation, cancel_reservation  # Import views

urlpatterns = [
    # URL to make a reservation
    path(
        'make-reservation/',
        make_reservation,
        name='make_reservation'
    ),

    # URL to cancel a reservation
    path(
        'cancel-reservation/<int:reservation_id>/',
        cancel_reservation,
        name='cancel_reservation'
    ),
]
