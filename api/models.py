from django.db import models

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField()

class Hamburguesa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)

