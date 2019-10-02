from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.permissions import IsAdminOrReadOnly
from .models import Category, SubCategory, Product
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

    def get_queryset(self):
        """
        overriding to activate lookup
        """
        categories = self.request.GET.get('categories')
        if categories:
            categories = categories.split(',')
            return Product.objects.filter(categories__id__in=categories, out_of_stock=False)

        queryset = Product.objects.all().prefetch_related()
        return queryset


class ProductRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateAPI view for Product model
    """
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Product.objects.all().prefetch_related()
    lookup_field = 'slug'
