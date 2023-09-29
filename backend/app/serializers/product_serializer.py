from rest_framework import serializers

from app.models import Category
from app.serializers import CategorySerializer


# ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source="category", queryset=Category.objects.all())
    category = CategorySerializer(read_only=True)
