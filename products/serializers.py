from rest_framework import serializers
from .models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for Category model
    """

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for SubCategory model
    """

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """

    class Meta:
        model = Product
        fields = '__all__'
