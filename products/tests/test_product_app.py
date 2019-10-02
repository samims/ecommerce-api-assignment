from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from products.models import Category, SubCategory
from products.serializers import (
    CategorySerializer,
    SubCategorySerializer,
)

User = get_user_model()


def create_category():
    return Category.objects.create(name="Topwear")


def create_sub_category():
    return SubCategory.objects.create(name="winter_wear", category=create_category())


class TestCategorySubCategoryAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='test_user', email="test@example.com", password='testpass')
        self.client.login(username="test_user", password="testpass")

    def test_create_category(self):
        base_url = reverse("products:category-list")
        response = self.client.post(base_url, data={"name": "Topwear", "slug": "top-wear"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category_list(self):
        base_url = reverse("products:category-list")
        self.client.post(base_url, data={"name": "Topwear"}, format='json')
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        response = self.client.get(base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data['results'])

    def test_create_subcategory(self):
        """
        Tests Sub Category Creation
        :return:
        """
        category_obj = create_category()
        base_url = reverse("products:subcategory-list")
        response = self.client.post(base_url, data={"name": "T-shirt", "category": category_obj.id},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subcategory_list(self):
        """
        Test of SubCategory returning proper data
        in list view
        """
        base_url = reverse("products:subcategory-list")
        self.client.post(base_url, data={"name": "T-shirt", 'category': create_category().id},
                         format='json')

        response = self.client.get(base_url)
        sub_categories = SubCategory.objects.all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data['results'])


class TestProductAPI(APITestCase):
    """
    Tests Product
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='test_user', email="test@example.com", password='testpass')
        self.client.login(username="test_user", password="testpass")

    def test_create_product(self):
        base_url = reverse("products:product_list")
        response = self.client.post(base_url, data={"name": "Puma", "price": 1000, "gender": "man",
                                                    "number_of_stock": 4, "categories": [create_category().id],
                                                    "sub_categories": [create_sub_category().id]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
