from django.shortcuts import render
from .serialazers import ProductSerializer
from .models import Product
# Create your views here.
from rest_framework import viewsets, generics           

#used that viewsets to provide CRUD operations for Product model
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListSlug(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        category_slug = self.kwargs['slug']        
        return Product.objects.filter(category_slug=category_slug)