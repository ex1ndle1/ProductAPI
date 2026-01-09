from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListByChildCategorySlug

app_name = 'shop'
router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = [ 
      path('products/category/<slug:slug>/', ProductListByChildCategorySlug.as_view(), name='products-by-category'),
]