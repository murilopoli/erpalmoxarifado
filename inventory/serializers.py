# inventory/serializers.py

from rest_framework import serializers
from .models import Product, WarehouseLocation, InventoryItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'created_at', 'updated_at']

class WarehouseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseLocation
        fields = ['id', 'code', 'description']

class InventoryItemSerializer(serializers.ModelSerializer):
    # Campos para LEITURA (mostra os objetos completos)
    product = ProductSerializer(read_only=True)
    location = WarehouseLocationSerializer(read_only=True)

    # Campos para ESCRITA (recebe apenas os IDs)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=WarehouseLocation.objects.all(), source='location', write_only=True
    )

    class Meta:
        model = InventoryItem
        # Define os campos que a API irá expor
        fields = [
            'id',
            'product',      # Para leitura
            'location',     # Para leitura
            'quantity',
            'last_updated',
            'product_id',   # Para escrita
            'location_id',  # Para escrita
        ]