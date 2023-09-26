from django.db import models


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=100)
