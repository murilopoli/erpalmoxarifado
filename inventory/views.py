# inventory/views.py

from rest_framework import viewsets
from .models import Product, WarehouseLocation, InventoryItem
from .serializers import ProductSerializer, WarehouseLocationSerializer, InventoryItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint para visualizar e editar produtos."""
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class WarehouseLocationViewSet(viewsets.ModelViewSet):
    """API endpoint para visualizar e editar localizações no armazém."""
    queryset = WarehouseLocation.objects.all().order_by('code')
    serializer_class = WarehouseLocationSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    """API endpoint para visualizar e editar o estoque de itens."""
    queryset = InventoryItem.objects.select_related('product', 'location').all()
    serializer_class = InventoryItemSerializer