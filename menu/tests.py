from django.test import TestCase
from django.urls import reverse
from .models import MenuItem

# Create your tests here.

# Menu item test
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
        self.assertEqual(response.status_code, 200)  # Check if the status code is 200 OK

    def test_menu_view_template(self):
        response = self.client.get(reverse('menu'))
        self.assertTemplateUsed(response, 'menu/menu.html')  # Check if the correct template is used

    def test_menu_view_context(self):
        response = self.client.get(reverse('menu'))
        self.assertIn('menu_items', response.context)  # Check if 'menu_items' is in the context
        self.assertEqual(len(response.context['menu_items']), 1)  # Verify that we have one menu item
        self.assertEqual(response.context['menu_items'][0].title, 'Test Item')  # Verify the item

class RedirectMenuViewTests(TestCase):

    def test_redirect_menu_html(self):
        response = self.client.get(reverse('redirect_menu_html'))
        self.assertEqual(response.status_code, 302)  # Check for a redirect status code
        self.assertRedirects(response, reverse('menu'))  # Ensure it redirects to the 'menu' URL