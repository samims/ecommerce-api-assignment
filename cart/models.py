from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save, m2m_changed
from products.models import Product

User = get_user_model()


class Cart(models.Model):
    """
    Cart model
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True, related_name='carts')
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(instance, action, sender, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        instance.total = total
        instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)
