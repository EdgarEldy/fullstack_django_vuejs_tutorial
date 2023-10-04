from django.db import models


# Customer model
class Customer(models.Model):
    first_name = models.CharField(unique=True, max_length=100, verbose_name="First Name")
    last_name = models.CharField(unique=True, max_length=100, verbose_name="Last Name")
    tel = models.CharField(unique=True, max_length=100, verbose_name="Telephone")
    email = models.CharField(unique=True, max_length=100, verbose_name="Email")
    address = models.CharField(max_length=100, verbose_name="Address")

    class Meta:
        db_table = 'app_customers'
        verbose_name_plural = "customers"
        ordering = ['id']
        default_permissions = []
