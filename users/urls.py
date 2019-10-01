from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from .views import RegisterAPIView

app_name = "users"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("api-token-auth/", obtain_jwt_token, name="obtain_token"),
    path("api-token-refresh/", refresh_jwt_token, name="refresh_token"),
    path("api-token-verify/", verify_jwt_token, name="verify_token"),
]
