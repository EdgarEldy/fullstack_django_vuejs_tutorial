from rest_framework import generics

from app.models import Product
from app.serializers import ProductSerializer


# Products generic views goes here
# List products, create a product
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# GetById, Update, Delete a product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer