from django.db import models

# Create your models here.
class Facturas(models.Model):
    id  = models.AutoField(primary_key=True)
    estudiante = models.IntegerField()
    institucion_asociada = models.IntegerField()
    responsable_economico = models.IntegerField()
    fecha_limite_pago = models.DateField()
    fecha_inicial = models.DateField()
    valor = models.FloatField()
    
    class Meta:
        db_table = 'facturas'
    
    