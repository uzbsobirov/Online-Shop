from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# This is base page 
class BasePage(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='base.html')


# <------------All of Product---------------->

#This class for Product View 
class ProductView(View):
    def get(self, request, *args, **kwargs):
        # We must get all items of Product model with all() method
        products = Product.objects.all().order_by('-date_created')
        paginator = Paginator(products, 5)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        # and we must give context for frontend
        return render(request=request, template_name='product/detail.html', context={'products': products, 'page': page})

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

# For EP(Edit Product)
class EditProduct(View):
    template_name = 'product/edit_product.html'

    def get(self, request, pk, *args, **kwargs):
        products = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=products)
        context = {
            'form': form,
            'pk': pk
        }
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, pk, *args, **kwargs):
        products = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=products)
        context = {
            'form': form,
            'pk': pk
        }
        if form.is_valid():
            form.save()
            return redirect('main:productview')
        return render(request=request, template_name=self.template_name, context=context)