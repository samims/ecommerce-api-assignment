from django.urls import path

from .views import OrderCreateView, TopUsersView

app_name = 'orders'

urlpatterns = [
    path("order/", OrderCreateView.as_view(), name='create'),
    path("order/max-user/", TopUsersView.as_view(), name="top_user")

]
