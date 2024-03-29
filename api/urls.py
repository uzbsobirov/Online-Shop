from django.urls import path
from .views import ProductsApiView, ProductApiView

app_name = 'api'

urlpatterns = [
    path('products/', ProductsApiView.as_view(), name='productsapi'),
    # One Product API View
    path('product/<int:pk>/', ProductApiView.as_view(), name='productapi')
]