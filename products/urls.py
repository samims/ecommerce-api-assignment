from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    SubCategoryViewSet,
    ProductListCreateAPI,
    ProductRetrieveUpdateDestroyAPI,
    CategorySumAPI
)

app_name = 'products'

router = DefaultRouter()
router.register("categories", CategoryViewSet, base_name='category')
router.register("subcategories", SubCategoryViewSet, base_name='subcategory')

urlpatterns = [
    path("", include(router.urls)),
    # path("categories",)
    path("products/", ProductListCreateAPI.as_view(), name='product_list'),
    path("products/<str:slug>/", ProductRetrieveUpdateDestroyAPI.as_view(), name='product_detail'),
    path("sum/", CategorySumAPI.as_view(), name='sum')
    # path('categories/search/', )
]
