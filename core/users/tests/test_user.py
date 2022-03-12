from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse


REGISTER_URL = reverse("register")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserTests(TestCase):
    """Test the users Model"""
    def setUp(self):
        self.client = Client()
        self.csrf_client = Client(enforce_csrf_checks=True)

        return super().setUp()

    def test_retrieving_register_url(self):
        """Test that the register url is reachable"""
        res = self.client.get(REGISTER_URL)
        self.assertTrue(res.status_code, 200)
