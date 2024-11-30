from django.urls import path
from . import views

urlpatterns = [
    path('todas', views.facturas),
]