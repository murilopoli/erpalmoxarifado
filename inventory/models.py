# inventory/models.py

from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True, verbose_name="SKU")
    name = models.CharField(max_length=255, verbose_name="Nome do Produto")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"

class WarehouseLocation(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Código do Endereço")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descrição do Local")

    def __str__(self):
        return self.code

class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    location = models.ForeignKey(WarehouseLocation, on_delete=models.CASCADE, verbose_name="Localização")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantidade")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        unique_together = ('product', 'location')
        verbose_name = "Item de Inventário"
        verbose_name_plural = "Itens de Inventário"

    def __str__(self):
        return f"{self.quantity} x {self.product.sku} @ {self.location.code}"