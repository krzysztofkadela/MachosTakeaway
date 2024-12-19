from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomerComment
from django.contrib.messages import get_messages

# Create your tests here.

User = get_user_model()

class CommentDeleteViewTests(TestCase):

    def setUp(self):
        # Create a user and a comment for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.comment = CustomerComment.objects.create(
            user=self.user,
            comment="This is a test comment.",  # Use the correct field name 'comment'
            is_approved=True,
        )

    def test_delete_comment_logged_in(self):
        """Test that logged-in user can delete their own comment."""
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_comment', args=[self.comment.id]))

        # Ensure the response is a redirect (302)
        self.assertEqual(response.status_code, 302)

        # Check that the comment is deleted
        with self.assertRaises(CustomerComment.DoesNotExist):
            self.comment.refresh_from_db()

        # Check that the success message is in the session
        messages = list(get_messages(response.wsgi_request))  # Get stored messages in the response
        self.assertTrue(any("Comment deleted successfully!" in str(message) for message in messages))

       # You could also assert redirection to the expected URL
        self.assertRedirects(response, reverse('user_comments'))  # Check redirect to user_comments page
