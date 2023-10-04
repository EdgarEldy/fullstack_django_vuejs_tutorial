from rest_framework import generics

from app.models import Customer
from app.serializers import CustomerSerializer


# Customers generic views goes here...
# List customers, create a customer
class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# GetById, Update, Delete a customer
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
