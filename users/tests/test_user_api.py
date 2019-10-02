from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

User = get_user_model()
AUTH_TOKEN_URL = reverse("users:obtain_token")
VERIFY_TOKEN_URL = reverse("users:verify_token")
REFRESH_TOKEN_URL = reverse("users:refresh_token")


class UserTest(APITestCase):
    def setUp(self):
        self.tes_user = User.objects.create_user(
            "test_user", "tests@example.com", "testpassword"
        )
        self.signup_url = reverse("users:register")
        self.data = {
            "email": "test1@example.com",
            "username": "test1",
            "password": "test1pass",
        }

    def test_create_user(self):
        """
        Test User is Creating and token is valid
        """

        response = self.client.post(self.signup_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        self.assertEqual(response.data["username"], response.data["username"])
        self.assertNotIn("password", response.data)

    def test_token_creation(self):
        """
        Tests token is being created
        """

        user = User.objects.create_user(**self.data)

        credentials = {"username": "test1", "password": "test1pass"}

        response = self.client.post(AUTH_TOKEN_URL, credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def get_token(self):
        client = APIClient()
        response = client.post(AUTH_TOKEN_URL, self.data, format='json')
        return response.data['token']

    def test_token_verification(self):
        """
        Test token verification
        """
        user = User.objects.create_user(**self.data)
        credentials = {"username": "test1", "password": "test1pass"}
        token = self.get_token()
        response = self.client.post(VERIFY_TOKEN_URL, {'token': token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_token_refresh(self):
        """
        Test token verification
        """
        user = User.objects.create_user(**self.data)
        credentials = {"username": "test1", "password": "test1pass"}
        token = self.get_token()
        response = self.client.post(REFRESH_TOKEN_URL, {'token': token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
