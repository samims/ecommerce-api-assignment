from rest_framework import serializers
from .models import Order
from cart.models import Cart


class OrderSerializer(serializers.ModelSerializer):
    """
    serializer for order model
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            "total": {"read_only": True},
            "cart": {"read_only": True}
        }

    def create(self, validated_data):
        """
        overriding to automatically fill cart
        """
        qs = Cart.objects.filter(user=self.context['request'].user, active=True)
        if qs:
            cart_obj = qs.first()
            if cart_obj.total:
                validated_data['cart'] = cart_obj
                return super(OrderSerializer, self).create(validated_data)
            raise serializers.ValidationError("add item to cart")
        raise serializers.ValidationError("no cart is available")
