from django.urls import path
from .views import OrderCreateView

app_name = 'orders'

urlpatterns = [
    path("order/", OrderCreateView.as_view(), name='create'),

]