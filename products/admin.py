from django.contrib import admin

# Register your models here.
from .models import Product

@admin.register(Product) # create the module 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'updated_at', )   # which is iin the display field.
    search_fields = ('id', 'name', 'price')  # which part of the filed is in the search filed.