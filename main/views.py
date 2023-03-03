from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import ProductForm

# This is base page 
class BasePage(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='base.html')


#This class for Product View 
class ProductView(View):
    def get(self, request, *args, **kwargs):
        # We must get all items of Product model with all() method
        products = Product.objects.all().order_by('date_created')
        # and we must give context for frontend
        return render(request=request, template_name='product/detail.html', context={'products': products})

# This class for ANP(Add New Product)
class AddProduct(View):
    template_name = 'product/add_product.html'

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request=request, template_name=self.template_name, context={'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:productview')
        else:
            return render(request=request, template_name=self.template_name, context={'form': form})

# This class for DP(Delete Product)
class DeleteProduct(View):
    template_name = 'product/delete.html'
    # Get function
    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        return render(request=request, template_name=self.template_name, context={'product': product, 'pk': pk})

# For Confirm Delete Product
class ConfirmDeleteProduct(View):
    # We must type get function for delete product
    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('main:productview')