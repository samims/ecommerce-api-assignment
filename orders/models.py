from django.db import models
from cart.models import Cart
from django.conf import settings
from django.db.models.signals import pre_save


class Order(models.Model):
    """
    order model
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    # redundant because asked in requirement
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp', ]


def order_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    pre save receiver for Order model
    """
    if not instance.total:
        instance.total = instance.cart.total
        instance.save()


pre_save.connect(order_pre_save_receiver, sender=Order)
