from django.shortcuts import render
from .serialazers import ProductSerializer
from .models import Product
# Create your views here.
from rest_framework import viewsets, generics           


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListByChildCategorySlug(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        category_slug = self.kwargs['slug']        
        return Product.objects.filter(category__slug=category_slug)