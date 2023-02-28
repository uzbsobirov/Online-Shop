from django.contrib import admin
from .models import (
    Product,
    Category
)

uneditable_fields = ('id', 'date_created', 'date_updated')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
        'description'
    )
    fields = [field.name for field in Category._meta.fields if field.name not in uneditable_fields]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
        'description',
        'product_id',
        'category'
    )
    fields = [field.name for field in Product._meta.fields if field.name not in uneditable_fields]