from django.shortcuts import render

from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingrediente


class HamburguesaViewSet(viewsets.ModelViewSet):
    queryset = Hamburguesa.objects.all().order_by('nombre')
    serializer_class = HamburguesaSerializer
    # lookup_url_kwarg = "asd"

    def retrieve(self, request, pk=None):
        if not isinstance(pk, int):
            return Response(
                {"code": "400", "descripcion": 'id invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = Hamburguesa.objects.all()
        hamburguesa = get_object_or_404(queryset, pk=pk)
        serializer = HamburguesaSerializer(hamburguesa)
        return Response(serializer.data)

    def create(self, request):
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"code": "201", "descripcion": 'operacion exitosa'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"code": "400", "descripcion": 'operacion fallida'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        if request.method == "GET":
            return Response(
                {"code": "200", "descripcion": 'resultados obtenidos'},
                status=status.HTTP_200_OK
            )
        elif request.method == "POST":
            return Response(
                {"code": "201", "descripcion": 'ingrediente cread0'},
                status=status.HTTP_201_CREATED
            )

    def partial_update(self, request, pk=None):
        try:
            aux = int(pk)
        except:
            return Response(
                {"code": "400", "descripcion": 'id invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            burguer = Hamburguesa.objects.get(id=pk)
        except:
            return Response(
                {"code": "404", "descripcion": 'hamburguesa inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )

        if "id" in request.data or "ingredientes" in request.data:
            return Response(
                {"code": "400", "descripcion": 'parametros invalidos'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = HamburguesaSerializer(
            burguer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"code": "200", "descripcion": 'operacion exitosa'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"code": "400", "descripcion": 'parametros invalidos'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        try:
            burguer = Hamburguesa.objects.get(id=pk)
        except:
            return Response(
                {"code": "201", "descripcion": 'hamburguesa creada'},
                status=status.HTTP_201_CREATED
            )
        burguer.delete()
        return Response(
            {"code": "404", "descripcion": 'hamburguesa inexistente'},
            status=status.HTTP_404_NOT_FOUND
        )

    @action(detail=True, methods=['put', 'delete'], url_path='ingrediente/(?P<pk2>[^/.]+)')
    def ingrediente(self, request, pk=None, pk2=None):
        try:
            burguer = Hamburguesa.objects.get(id=pk)
        except:
            return Response(
                {"code": "400", "descripcion": 'Id de hamburguesa inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if request.method == 'PUT':
            try:
                ingredient = Ingrediente.objects.get(id=pk2)
            except:
                return Response(
                    {"code": "404", "descripcion": 'ingrediente inexistente'},
                    status=status.HTTP_404_NOT_FOUND
                )
            burguer.ingredientes.add(ingredient)
            return Response(
                {"code": "201", "descripcion": 'ingrediente agregado'},
                status=status.HTTP_404_NOT_FOUND
            )
        if request.method == 'DELETE':
            try:
                ingredient = Ingrediente.objects.get(id=pk2)
                burguer.ingredientes.remove(ingredient)
            except:
                return Response(
                    {"code": "404", "descripcion": 'Ingrediente inexistente en la hamburguesa'},
                    status=status.HTTP_404_NOT_FOUND
                )
            # burguer.save()
            return Response(
                {"code": "200", "descripcion": 'Ingrediente retirado'},
                status=status.HTTP_200_OK
            )


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all().order_by('nombre')
    serializer_class = IngredienteSerializer

    def retrieve(self, request, pk=None):
        if not isinstance(pk, int):
            return Response(
                {"code": "400", "descripcion": 'id invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = Ingrediente.objects.all()
        ingrediente = get_object_or_404(queryset, pk=pk)
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    def create(self, request):
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"code": "201", "descripcion": 'Ingrediente Creado'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"code": "400", "descripcion": 'Input Invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, id=None):
        if request.method == "GET" or request.method == "get":
            return Response(
                {"code": "200", "descripcion": 'resultados obtenidos'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"code": "201", "descripcion": 'ingrediente cread0'},
                status=status.HTTP_201_CREATED
            )

    def partial_update(self, request, id=None):
        try:
            aux = int(id)
        except:
            return Response(
                {"code": "400", "descripcion": 'id invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            ingredient = Ingrediente.objects.get(id=id)
        except:
            return Response(
                {"code": "404", "descripcion": 'ingrediente inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {"code": "200", "descripcion": 'operacion exitosa'},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        try:
            ingredient = Ingrediente.objects.get(id=pk)
        except:
            return Response(
                {"code": "404", "descripcion": 'ingrediente inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        burguers = ingredient.hamburguesa_set.all()
        if not burguers:
            ingredient.delete()
            return Response(
                {"code": "200", "descripcion": 'ingrediente eliminado'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"code": "409", "descripcion": 'Ingredientee no se puede borrar, se encuentra presente en una hamburguesa'},
                status=status.HTTP_409_CONFLICT
            )
