from rest_framework import serializers

from app.models import Customer


# OrderSerializer
class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(source="customer", queryset=Customer.objects.all())
