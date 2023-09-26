from django.db import models

from app.models import Category


# Product model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=False, )
    product_name = models.CharField(max_length=100, unique=True)
    unit_price = models.FloatField()

    class Meta:
        db_table = 'app_products'
        index_together = unique_together = [['category', 'product_name']]
        verbose_name_plural = 'products'
        ordering = ['category', 'product_name']
        default_permissions = []
