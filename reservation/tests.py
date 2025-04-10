from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from .models import Reservation, RestaurantSettings
from datetime import datetime, timedelta

User = get_user_model()


class ReservationViewTests(TestCase):

    def setUp(self):
        """
        Set up a test user and restaurant settings before each test.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.settings = RestaurantSettings.objects.create(
            opening_time='10:00',
            closing_time='22:00'
        )

    def test_make_reservation(self):
        """
        Test that a logged-in user can create a reservation and
        receives a success message.
        """
        booking_date = (datetime.now() + timedelta(days=2)).date()

        response = self.client.post(reverse('make_reservation'), {
            'number_of_guests': 4,
            'contact_number': '1234567890',
            'booking_date': booking_date,
            'booking_time': '19:00',
            'special_requests': 'Window table',
        })

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Reservation.objects.filter(
            user=self.user,
            booking_date=booking_date,
            booking_time='19:00',
            number_of_guests=4,
            contact_number='1234567890',
            special_requests='Window table'
        ).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Your reservation has been made successfully!" in str(msg)
            for msg in messages
        ))

    def test_cancel_reservation(self):
        """
        Test that a user can cancel their own reservation.
        """
        reservation = Reservation.objects.create(
            user=self.user,
            number_of_guests=3,
            contact_number='0987654321',
            booking_date=datetime.now().date(),
            booking_time='20:00'
        )

        response = self.client.post(
            reverse('cancel_reservation', args=[reservation.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Reservation.objects.filter(id=reservation.id).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Reservation has been cancelled successfully!" in str(msg)
            for msg in messages
        ))
