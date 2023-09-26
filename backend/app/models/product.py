from django.db import models

from app.models import Category


# Product model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE(), related_name="products", null=False, )
    product_name = models.CharField(max_length=100, unique=True)
    unit_price = models.FloatField()
