from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('', BasePage.as_view(), name='basepage'),
    path('products/', ProductView.as_view(), name='productview'),
    # Add New Product
    path('add_product/', AddProduct.as_view(), name='addproduct'),
    # Delete Product
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='deleteproduct')
]