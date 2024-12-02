from django.urls import path
from . import views

urlpatterns = [
    path('obtener_facturas/', views.obtener_facturas),
    path('facturas_por_fecha/', views.facturas_por_fecha),
]