from django.db import models


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = 'app_categories'
        ordering = ['id']
        default_permissions = []
