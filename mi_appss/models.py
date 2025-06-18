from django.db import models

# Tablas Consultas.

class SolicitudCredito(models.Model):
    nombre_apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    email = models.EmailField()
    celular = models.CharField(max_length=20)
    ingreso_mensual = models.DecimalField(max_digits=12, decimal_places=2)
    valor_propiedad = models.DecimalField(max_digits=12, decimal_places=2)
    ahorros = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_envio = models.DateTimeField(auto_now_add=True)