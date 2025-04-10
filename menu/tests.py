from django.test import TestCase
from django.urls import reverse
from .models import MenuItem


class MenuViewTests(TestCase):

    def setUp(self):
        # Set up test data with correct field names
        self.menu_item = MenuItem.objects.create(
            title='Test Item',
            description='A delicious test item.',
            price=10.99,
            category='burger',
            image=None  # or provide a valid image if required
        )

    def test_menu_view_status_code(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_menu_view_template(self):
        response = self.client.get(reverse('menu'))
        self.assertTemplateUsed(response, 'menu/menu.html')

    def test_menu_view_context(self):
        response = self.client.get(reverse('menu'))
        self.assertIn('menu_items', response.context)
        self.assertEqual(len(response.context['menu_items']), 1)
        self.assertEqual(
            response.context['menu_items'][0].title, 'Test Item'
        )


class RedirectMenuViewTests(TestCase):

    def test_redirect_menu_html(self):
        response = self.client.get(reverse('redirect_menu_html'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('menu'))
