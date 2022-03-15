from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

REGISTER_URL = reverse("register")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserTests(TestCase):
    """Test the users Model"""

    def test_retrieving_register_url(self):
        """Test that the register url is reachable"""
        res = self.client.get(REGISTER_URL)
        self.assertTrue(res.status_code, 200)

    def test_that_an_user_is_created(self):
        """Test that an user is created successfully"""
        payload = {
            'email': 'test@test.com',
            'password': 'password123',
        }

        create_user(**payload)

        queryset = get_user_model().objects.get(id=1)

        self.assertEqual(queryset.email, payload['email'])
        self.assertTrue(queryset.check_password(payload['password']))

    def test_user_exists(self):
        """Test that an user that exists cannot be saved"""
        payload = {
            'email': 'test@test.com',
            'password': 'password123',
        }
        payload2 = {
            'email': 'test@test.com',
            'password': 'abcdewsqs12',
        }

        create_user(**payload)
        create_user(**payload2)

        user_count = get_user_model().objects.all().count()

        self.assertEqual(user_count, 1)
