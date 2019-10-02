from django.contrib.auth import get_user_model
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "email", "password")
        extra_kwargs = {
            "password": {"style": {"input_type": "password"}, "write_only": True}
        }

    def create(self, validated_data):
        """
        overriding to avoid storing raw text password
        """
        user = get_user_model().objects.create_user(**validated_data)
        validated_data.pop("password")
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    serializer for User model
    """
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )
