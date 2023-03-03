from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('', BasePage.as_view(), name='basepage'),
    path('products/', ProductView.as_view(), name='productview'),
    # Add New Product
    path('add_product/', AddProduct.as_view(), name='addproduct'),
    # Delete Product
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='deleteproduct'),
    #Confirm Delete Product
    path('confirm/delete/<int:pk>/', ConfirmDeleteProduct.as_view(), name='confirmdeleteproduct'),
    # Edit Product
    path('edit/product/<int:pk>/', EditProduct.as_view(), name='editproduct')
]