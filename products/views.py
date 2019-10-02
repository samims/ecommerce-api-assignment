from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, SubCategory, Product
from core.permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet fo Category model
    """
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Category.objects.all().order_by('id')


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for SubCategory model
    """
    serializer_class = SubCategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = SubCategory.objects.all().order_by('id')


class ProductListCreateAPI(ListCreateAPIView):
    """
    ListCreate View for Product model
    """
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Product.objects.all().prefetch_related().order_by('id')


class ProductRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateAPI view for Product model
    """
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Product.objects.all().prefetch_related().order_by('id')
    lookup_field = 'slug'


