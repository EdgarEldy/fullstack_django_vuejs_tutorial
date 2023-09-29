from rest_framework import serializers

from app.models import Customer, Product


# OrderSerializer
class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(source="customer", queryset=Customer.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(source="product", queryset=Product.objects.all())
