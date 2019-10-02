from rest_framework import serializers
from .models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for Category model
    """

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'slug': {'read_only': True}
        }


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
        extra_kwargs = {
            'slug': {'read_only': True},
            'out_of_stock': {'read_only': True}
        }

    def to_representation(self, instance):
        """
        overriding to show category & sub category
        detail in product
        """
        representation = super(ProductSerializer, self).to_representation(instance)
        categories = instance.categories.all()
        categories = CategorySerializer(categories, many=True)
        representation['categories'] = categories.data

        representation['sub_categories'] = SubCategorySerializer(instance.sub_categories.all(), many=True).data
        return representation
