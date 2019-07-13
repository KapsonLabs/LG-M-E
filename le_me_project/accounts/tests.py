from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model

from accounts import views

class TestAccounts(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.factory = APIRequestFactory()
        self.view = views.UserAuthenticate.as_view()
        self.uri = '/auth/login/'

    @staticmethod
    def setup_user():
        User = get_user_model()
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
        request = self.factory.post(self.uri, params)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                        'Expected Response code 200, got {0}'.format(response.status_code))
