from rest_framework import serializers

from api.models import Ingrediente, Hamburguesa


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')

class IngredientePathSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    class Meta:
        model = Ingrediente
        fields = ['path']

class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = IngredientePathSerializer(read_only=True, many=True)
    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'descripcion', 'precio', 'imagen', 'ingredientes')
