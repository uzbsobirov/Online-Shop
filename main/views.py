from django.shortcuts import render
from django.views import View
from .models import *


class BasePage(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='base.html')

class ProductView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request=request, template_name='product/detail.html', context={'products': products})