from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from django.urls import reverse

from .serializers import DistrictListSerializer, DistrictCreateSerializer
from .models import District

class BaseViewTest(APITestCase):
    client = APIClient()
    uri = 'district_list_view'

    def setUp(self):
        #add some test data
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.create_district(self.user, "Kampala", "EASTERN", 2)
        self.create_district(self.user, "Masaka", "WESTERN", 5)

    @staticmethod
    def create_district(created_by ,district_name, district_region, district_size_hectares):
        if district_name != "" and district_region != "":
            if isinstance(district_name, str) and isinstance(district_region, str) and isinstance(district_size_hectares, int):
                District.objects.create(created_by=created_by, district_name=district_name, district_region=district_region, district_size_hectares=district_size_hectares)

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test',
            email='testuser@test.com',
            password='test1234',
            is_administrator=True
        )


class TestGetAllDistricts(BaseViewTest):
    
    def test_list_all_districts(self):
        # self.client.login(username="test", password="test1234")
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.get(reverse(self.uri))

        #fetch test data from the database
        expected = District.objects.all()
        serialized = DistrictListSerializer(expected, many=True)
        #self.assertEqual(serialized.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestCreateDistricts(APITestCase):

    def test_create_district(self):
        params = {
            "district_name":"Kampala",
            "district_region":"EASTERN",
            "district_size_hectares":2
        }
        response = self.client.post(reverse('district_create_view'), params)
        serialized = DistrictCreateSerializer(params)
        self.assertEqual(serialized.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
