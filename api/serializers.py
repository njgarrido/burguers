from rest_framework import serializers
from django.urls import reverse
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
    def get_path(self, ingrediente):
        return 'https://burguersnj.herokuapp.com{}'.format(reverse('ingrediente',args=[ingrediente.id]))

class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = IngredientePathSerializer(read_only=True, many=True)
    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'descripcion', 'precio', 'imagen', 'ingredientes')
