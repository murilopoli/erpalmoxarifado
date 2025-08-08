# core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rota principal da nossa API de inventário
    path('api/inventory/', include('inventory.urls')),
]