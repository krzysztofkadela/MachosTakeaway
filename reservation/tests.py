from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Reservation
from datetime import datetime, timedelta

User = get_user_model()

class ReservationViewTests(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_make_reservation(self):
        """Test that a logged-in user can create a reservation."""
        response = self.client.post(reverse('make_reservation'), {
            'number_of_guests': 4,
            'contact_number': '1234567890',
            'booking_date': (datetime.now() + timedelta(days=2)).date(),  # Booking for two days later
            'booking_time': '19:00',
            'special_requests': 'Window table',
        })
        
        # Check for a redirection after submitting the reservation
        self.assertEqual(response.status_code, 302)
        
        # Ensure the reservation was created
        self.assertTrue(Reservation.objects.filter(user=self.user, booking_date=(datetime.now() + timedelta(days=2)).date(), booking_time='19:00').exists())

    def test_cancel_reservation(self):
        """Test that a user can cancel their own reservation."""
        # Create a reservation to cancel
        reservation = Reservation.objects.create(
            user=self.user,
            number_of_guests=3,
            contact_number='0987654321',
            booking_date=datetime.now().date(),
            booking_time='20:00'
        )

        response = self.client.post(reverse('cancel_reservation', args=[reservation.id]))
        
        # Check if the reservation was deleted
        self.assertEqual(response.status_code, 302)  # Should redirect after canceling
        self.assertFalse(Reservation.objects.filter(id=reservation.id).exists())  # Check reservation was deleted
