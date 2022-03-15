from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

CONTACTS_URL = reverse("contacts")
UPLOAD_FILE_URL = reverse('process-file')


def create_sample_user():
    """Creates a sample user for tests"""
    return get_user_model().objects.create_user(
        email='user@test.com', password='password123'
    )


class ContactsTestsPublic(TestCase):
    """Test the contact public access"""

    def test_auth_required(self):
        """Test that the authentication is required"""
        res = self.client.get(CONTACTS_URL)
        self.assertEqual(res.status_code, 302)
