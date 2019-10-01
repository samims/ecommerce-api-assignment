from django.contrib import admin
from .models import SubCategory, Category, Product

admin.site.register((SubCategory, Category, Product))
