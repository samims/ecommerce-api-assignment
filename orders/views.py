from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderSerializer
from .models import Order


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
