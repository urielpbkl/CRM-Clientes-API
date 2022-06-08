from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Clientes(models.Model):
    nombre = CharField(max_length=40)
    empresa = CharField(max_length=40)
    email = CharField(max_length=40)
    telefono = models.IntegerField(null=True)
    notas = CharField(max_length=4000)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id'] #ORDENAR PONIENDO PRIMERO LOS ÚLTIMOS ARTÍCULOS PUBLICADOS 

    def __str__(self):
        return self.nombre 



