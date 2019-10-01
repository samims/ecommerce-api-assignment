from django.db import models
from django.db.models.signals import pre_save

from core.utils import unique_slug_generator

GENDER_CHOICES = (
    ("man", "man"),
    ("woman", "woman"),
    ("unisex", "unisex")
)


class Category(models.Model):
    """
    Category model
    """

    name = models.CharField(max_length=100, db_index=True, blank=False)
    slug = models.SlugField(max_length=254, db_index=True, blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """
    Subcategory model
    """

    name = models.CharField(max_length=100, blank=False, null=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, related_name='sub_categories')
    slug = models.SlugField(max_length=254, db_index=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    product model
    """

    name = models.CharField(max_length=254, blank=False, null=True)
    slug = models.CharField(max_length=254, blank=True, null=True, unique=True)
    price = models.DecimalField(blank=False, decimal_places=2, max_digits=9, default=0.0)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, db_index=True)
    out_of_stock = models.BooleanField(default=True)
    number_of_stock = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True)


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    pre save receiver for Category model
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)


def sub_category_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    pre save receiver for SubCategory model
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(sub_category_pre_save_receiver, sender=SubCategory)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    pre save receiver for Product model
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    if instance.number_of_stock and instance.out_of_stock:
        instance.out_of_stock = False


pre_save.connect(product_pre_save_receiver, sender=Product)
