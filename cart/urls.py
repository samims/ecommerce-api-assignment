from django.urls import path
from .views import CartAPIView, CartUpdateAPIView, RemoveProductFromCartAPI

app_name = "cart"

urlpatterns = [
    path("", CartAPIView.as_view(), name="home"),
    path("update/<int:pk>/", CartUpdateAPIView.as_view(), name="update"),
    path("remove-item/<str:slug>", RemoveProductFromCartAPI.as_view(), name="remove_product"),
]
