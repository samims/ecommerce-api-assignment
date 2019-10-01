from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    SubCategoryViewSet,
    ProductListCreateAPI,
    ProductRetrieveUpdateDestroyAPI,
)

app_name = 'products'

router = DefaultRouter()
router.register("categories", CategoryViewSet, base_name='category')
router.register("subcategories", SubCategoryViewSet, base_name='subcategory')

urlpatterns = [
    path("", include(router.urls)),
    path("products/", ProductListCreateAPI.as_view(), name='product_list'),
    path("products/<str:slug>/", ProductRetrieveUpdateDestroyAPI.as_view(), name='product_detail'),

]
