from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsOwner
from products.models import Product
from .models import Cart
from .serializers import CartSerializer, CartUpdateSerializer


class CartAPIView(GenericAPIView):
    """
    Cart Create API, creates cart if there is 
    no active cart available for the user
    """
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user, active=True)
        return queryset

    def get(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset()).prefetch_related()
        # if active cart already exists
        if qs:
            instance = qs.first()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data={"user": request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class CartUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CartUpdateSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user, active=True).prefetch_related()
        if queryset:
            # this repeated code as CartAPI can be
            # reduced using model manager
            return queryset
        Cart.objects.create(user=self.request.user)
        queryset = Cart.objects.filter(user=self.request.user, active=True).prefetch_related()
        return queryset


class RemoveProductFromCartAPI(GenericAPIView):
    serializer_class = CartUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user, active=True)
        return queryset

    def delete(self, request, *args, **kwargs):
        prod_obj = get_object_or_404(Product, slug=kwargs.get('slug'))
        qs = self.filter_queryset(self.get_queryset())
        if qs:
            qs.first().products.remove(prod_obj)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
