from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomerComment
from django.contrib.messages import get_messages
from .forms import CustomerCommentForm # For edit comment view test.

# Create your tests here.

# Delete comment test 

User = get_user_model()

class CommentDeleteViewTests(TestCase):

    def setUp(self):
        # Create a user and a comment for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.comment = CustomerComment.objects.create(
            user=self.user,
            comment="This is a test comment.",  # comment
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

       # Redirection to the expected URL(user_comments)
        self.assertRedirects(response, reverse('user_comments'))  # Check redirect to user_comments page

# Delete comment test end

# Edit comment test

class EditCommentViewTests(TestCase):

    def setUp(self):
        # Create a user and a comment for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.comment = CustomerComment.objects.create(
            user=self.user,
            comment="This is a test comment.",
            is_approved=True,
        )
        self.client.login(username='testuser', password='testpass')

    def test_edit_comment_logged_in(self):
        """Test that logged-in user can edit their own comment."""
        response = self.client.post(reverse('edit_comment', args=[self.comment.id]), {
            'comment': 'This is an updated test comment.'
        })
        
        # Check that the response redirects
        self.assertEqual(response.status_code, 302)  # Should redirect after saving

        # Verify that the comment was updated in the database
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.comment, 'This is an updated test comment.')

        # Check for a success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Your comment has been updated successfully!" in str(message) for message in messages))

    def test_edit_other_users_comment(self):
        """Test that a user cannot edit another user's comment."""
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        other_comment = CustomerComment.objects.create(
            user=other_user,
            comment="This is another user's comment.",
            is_approved=True,
        )
        
        # Attempt to edit the comment that does not belong to the logged-in user
        response = self.client.post(reverse('edit_comment', args=[other_comment.id]), {
            'comment': 'Trying to edit another user\'s comment.'
        })
        
        # Check if the response is 404, since the user should be unable to access that comment
        self.assertEqual(response.status_code, 404)

    def test_edit_comment_template_loads_correctly(self):
        """Test that the edit comment page loads with the correct context."""
        response = self.client.get(reverse('edit_comment', args=[self.comment.id]))
        
        # Verify the correct template was used
        self.assertEqual(response.status_code, 200)  # Should successfully load the edit page
        self.assertTemplateUsed(response, 'edit_comment.html')

        # Check that the form is populated with the current comment data
        self.assertIsInstance(response.context['form'], CustomerCommentForm)
        self.assertEqual(response.context['form'].instance, self.comment)  # The form's instance should be the comment object