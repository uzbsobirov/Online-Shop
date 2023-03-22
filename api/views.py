from django.shortcuts import render, get_object_or_404
from .serializers import ProductSerializer
from main.models import Product
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

# <-------------------Product Serializer------------------------>
class ProductsApiView(APIView, PageNumberPagination):
    """
    Products API View
    """
    serializer_class = ProductSerializer
    page_size = 3

    # `get` function
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        result = self.paginate_queryset(products, request, view=self)
        serializer = self.serializer_class(instance=result, many=True)
        return self.get_paginated_response(serializer.data)

# API for Get one product
class ProductApiView(APIView):
    """
    One Product API View
    """
    # Seriaizer class
    serializer_class = ProductSerializer


    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product)
        return Response(data=serializer.data)


    def delete(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(data={'Deleted': 'Product was succesfully deleted'}, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk, *args, **kwargs):
        data = request.data
        product = get_object_or_404(Product, pk=pk)
        serializer = self.serializer_class(instance=product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    
    def patch(self, request, pk, *args, **kwargs):
        data = request.data
        product = get_object_or_404(Product, pk=pk)
        serializer = self.serializer_class(instance=product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
