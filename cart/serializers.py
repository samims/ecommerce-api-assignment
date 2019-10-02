from rest_framework import serializers

from users.serializers import UserSerializer
from products.serializers import ProductSerializer

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    """
    serializer for Cart
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1


class CartUpdateSerializer(serializers.ModelSerializer):
    """
    serializer for Cart update
    """

    user = UserSerializer(read_only=True)

    # products = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
        # depth = 1
        extra_kwargs = {
            'product':
                {'allow_null': False, 'allow_blank': False, 'read_only': True},
            'total':
                {'read_only': True},
            'active':
                {'read_only': True}
        }
