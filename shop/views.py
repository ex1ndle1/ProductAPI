from django.shortcuts import render
from .serialazers import ProductSerializer
from .models import Product
# Create your views here.
from rest_framework import viewsets, generics           

#used that viewsets to provide CRUD operations for entire product model
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
class ProductListSlug(generics.ListAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return Product.objects.filter(category__slug=category_slug)