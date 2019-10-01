from rest_framework import generics
from .permissions import AnonPermissionOnly
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterAPIView(APIView):
    """
    View for SignUp
    AnonPermission is making sure
    that only anonymous Registers
    """

    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.filter(is_active=True)
    permission_classes = (AnonPermissionOnly,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data.pop("password")  # pass should not be in response
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
