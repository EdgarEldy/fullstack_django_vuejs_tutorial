from django.db import models

from app.models import Customer, Product


# Order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customers", null=False, )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products", null=False, )
    quantity = models.FloatField()
    total = models.FloatField()

    class Meta:
        db_table = "app_orders"
        verbose_name_plural = "orders"
        ordering = ["customer"]
        default_permissions = []
