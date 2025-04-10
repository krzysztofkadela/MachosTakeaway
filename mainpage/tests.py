from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages

from .models import CustomerComment
from .forms import CustomerCommentForm  # For edit comment view test

User = get_user_model()


class CommentDeleteViewTests(TestCase):
    def setUp(self):
        """Set up a test user and a comment."""
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.comment = CustomerComment.objects.create(
            user=self.user,
            comment="This is a test comment.",
            is_approved=True,
        )

    def test_delete_comment_logged_in(self):
        """Test that logged-in user can delete their own comment."""
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('delete_comment', args=[self.comment.id])
        )

        # Ensure redirect
        self.assertEqual(response.status_code, 302)

        # Check that the comment is deleted
        with self.assertRaises(CustomerComment.DoesNotExist):
            self.comment.refresh_from_db()

        # Confirm success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Comment deleted successfully!" in str(m) for m in messages
        ))

        # Check redirect to user_comments
        self.assertRedirects(response, reverse('user_comments'))


class EditCommentViewTests(TestCase):
    def setUp(self):
        """Set up a test user and a comment."""
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.comment = CustomerComment.objects.create(
            user=self.user,
            comment="This is a test comment.",
            is_approved=True,
        )
        self.client.login(username='testuser', password='testpass')

    def test_edit_comment_logged_in(self):
        """Test that logged-in user can edit their own comment."""
        response = self.client.post(
            reverse('edit_comment', args=[self.comment.id]),
            {'comment': 'This is an updated test comment.'}
        )

        # Should redirect after saving
        self.assertEqual(response.status_code, 302)

        # Confirm update in DB
        self.comment.refresh_from_db()
        self.assertEqual(
            self.comment.comment, 'This is an updated test comment.'
        )

        # Confirm success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Your comment has been updated successfully!" in str(m)
            for m in messages
        ))

    def test_edit_other_users_comment(self):
        """Test that a user cannot edit another user's comment."""
        other_user = User.objects.create_user(
            username='otheruser', password='otherpass'
        )
        other_comment = CustomerComment.objects.create(
            user=other_user,
            comment="This is another user's comment.",
            is_approved=True,
        )

        response = self.client.post(
            reverse('edit_comment', args=[other_comment.id]),
            {'comment': 'Trying to edit another user\'s comment.'}
        )

        # Should return 404 (not found)
        self.assertEqual(response.status_code, 404)
