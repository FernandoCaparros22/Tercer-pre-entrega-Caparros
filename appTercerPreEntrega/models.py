from django.db import models

# Create your models here.

class usuario(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
  
class propiedades(models.Model):

    pais = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    metrosCubiertos = models.FloatField()

class inversores(models.Model):

    email = models.EmailField()
    divisa = models.CharField(max_length=40) 
    cantInvertir = models.IntegerField()



