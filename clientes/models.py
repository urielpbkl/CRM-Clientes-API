from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)
    notas = models.CharField(max_length=4000)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id'] #ORDENAR PONIENDO PRIMERO LOS ÚLTIMOS ARTÍCULOS PUBLICADOS 

    def __str__(self):
        return self.nombre 



