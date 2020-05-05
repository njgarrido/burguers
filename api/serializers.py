from rest_framework import serializers

from api.models import Ingrediente, Hamburguesa

class HamburguesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'descripcion', 'precio', 'imagen', 'ingredientes')

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')