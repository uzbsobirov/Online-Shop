from django import forms
from .models import Product, Category

# Let me type form for Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price', 'status')