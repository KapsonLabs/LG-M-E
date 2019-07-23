from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, APIClient
from accounts.models import User
from django.urls import reverse

from accounts import views

class TestAccounts(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client = APIClient()
        self.uri = 'login-endpoint'

    @staticmethod
    def setup_user():
        return User.objects.create_user(
            username='test',
            email='testuser@test.com',
            password='test'
        )

    def test_authentication(self):
        params= {
            "username":"test",
            "password":"test"
        }
        response = self.client.post(reverse('login-endpoint'), params)
        self.assertEqual(response.status_code, 200,
                        'Expected Response code 200, got {0}'.format(response.status_code))
