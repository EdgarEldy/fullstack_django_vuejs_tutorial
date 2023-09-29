from rest_framework import serializers

from app.models import Customer, Product
from app.serializers import CustomerSerializer, ProductSerializer


# OrderSerializer
class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(source="customer", queryset=Customer.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(source="product", queryset=Product.objects.all())
    customer = CustomerSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
