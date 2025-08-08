# inventory/admin.py

from django.contrib import admin
from .models import Product, WarehouseLocation, InventoryItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'created_at')
    search_fields = ('sku', 'name')

@admin.register(WarehouseLocation)
class WarehouseLocationAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')
    search_fields = ('code',)

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'quantity', 'last_updated')
    search_fields = ('product__sku', 'product__name', 'location__code')
    list_filter = ('location',)