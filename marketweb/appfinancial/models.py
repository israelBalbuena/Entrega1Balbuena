from django.db import models

# Create your models here.

class Crypto(models.Model):
    nombre = models.CharField(max_length= 20)
    valor = models.FloatField()

class Raices(models.Model):
    Estado = models.CharField(max_length= 50)
    metros = models.IntegerField()
    valor  = models.FloatField()
    ubicacion = models.CharField(max_length= 50)

class acciones(models.Model):
    Empresa = models.CharField(max_length=50)
    valor_empresa = models.FloatField()
    valor_accion = models.FloatField()
    
