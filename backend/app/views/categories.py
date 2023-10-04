from rest_framework import generics

from app.models import Category
from app.serializers import CategorySerializer


# Generic views goes here...
# Retrieve and create
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
