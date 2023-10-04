from rest_framework import generics

from app.models import Order
from app.serializers import OrderSerializer


# Orders generic views goes here...
# List orders, create a new order
class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
