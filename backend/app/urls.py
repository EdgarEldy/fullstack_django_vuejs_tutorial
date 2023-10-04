"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import categories, products, customers, orders

urlpatterns = [
    # app urls goes here...
    # categories routes
    path('categories', categories.CategoryListView.as_view()),  # list, create routes
    path('categories/<int:pk>', categories.CategoryDetailView.as_view()),  # GetById, Update, Delete routes

    # products routes
    path('products', products.ProductListView.as_view()),  # list, create routes
    path('products/<int:pk>', products.ProductDetailView.as_view()),  # GetById, Update, Delete routes

    # customers routes
    path('customers', customers.CustomerListView.as_view()),  # list, create routes
    path('customers/<int:pk>', customers.CustomerDetailView.as_view()),  # GetById, Update, Delete routes

    # orders routes
    path('orders', orders.OrderListView.as_view()),  # list, create routes
    path('orders/<int:pk>', orders.OrderDetailView.as_view()),  # GetById, Update, Delete routes
]
