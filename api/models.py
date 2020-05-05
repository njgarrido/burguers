from django.db import models

class Ingrediente(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
class IngredienteEnHamburguesa(models.Model):
    path = models.TextField()

class Hamburguesa(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.TextField()
    ingredientes = models.ManyToManyField(IngredienteEnHamburguesa)