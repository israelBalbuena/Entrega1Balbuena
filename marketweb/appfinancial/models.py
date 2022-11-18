from django.db import models

# Create your models here.

class Crypto(models.Model):
    name = models.CharField(max_length= 20)
    value = models.FloatField(blank=True, null=True)
    market_price = models.FloatField(blank=True, null=True)
    number_of_coins = models.IntegerField(blank=True, null=True)

class Raices(models.Model):
    Estado = models.CharField(max_length= 50)
    metros = models.IntegerField()
    valor  = models.FloatField()
    ubicacion = models.CharField(max_length= 50)

class Acciones(models.Model):
    Empresa = models.CharField(max_length=50)
    valor_empresa = models.FloatField()
    valor_accion = models.FloatField()
    
