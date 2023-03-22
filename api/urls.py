from django.urls import path
from .views import ProductsApiView, ProductApiView

urlpatterns = [
    path('products/', ProductsApiView.as_view(), name='productsapi'),
    # One Product API View
    path('product/<int:pk>/', ProductApiView.as_view(), name='productapi')
]