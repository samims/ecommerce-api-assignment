from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db.models import Count, Sum
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from users.serializers import UserSerializer
from .models import Order
from .serializers import OrderSerializer

User = get_user_model()


class OrderCreateView(GenericAPIView):
    """
    View for Order Creation
    """

    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create_order(request, *args, **kwargs)

    def create_order(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TopUsersAPIView(GenericAPIView):
    """
    View to find top user
    """

    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        top_order_users = (
            User.objects.filter(
                order__timestamp__gte=timezone.now() - timedelta(days=30)
            )
            .annotate(order_count=Count("order"))
            .order_by("-order_count")
        )
        top_order_users = self.get_serializer(top_order_users, many=True).data
        data = {"top_order_users": top_order_users}
        top_value_users = (
            User.objects.filter(
                order__timestamp__gte=timezone.now() - timedelta(days=30)
            )
            .annotate(value_sum=Sum("order__total"))
            .order_by("-value_sum")
        )
        top_value_users = self.get_serializer(top_value_users, many=True).data
        data["top_value_users"] = top_value_users
        return Response(data, status=200)
