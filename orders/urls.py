from django.urls import path

from .views import OrderCreateView, TopUsersAPIView

app_name = 'orders'

urlpatterns = [
    path("order/", OrderCreateView.as_view(), name='create'),
    path("order/top-users/", TopUsersAPIView.as_view(), name="top_user")

]
