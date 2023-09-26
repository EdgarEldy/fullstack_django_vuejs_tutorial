from django.db import models

from app.models import Customer


# Order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customers", null=False, )
