# inventory/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WarehouseLocationViewSet, InventoryItemViewSet

# O Router do DRF cria as rotas de GET, POST, PUT, PATCH, DELETE automaticamente
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'locations', WarehouseLocationViewSet)
router.register(r'items', InventoryItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]