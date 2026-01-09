from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListSlug

app_name = 'shop'
router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = [ 
    path('', include(router.urls)),
      path('products/category/<slug:slug>/', ProductListSlug.as_view(), name='products-by-category'),
]