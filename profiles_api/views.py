from email import message
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """ API VIEW  de Prueba"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """retornar lista de caracteristicas de APIView"""
        an_apiview =[
            'usamos metodos HTTP como funciones (getm post, patch, put, delete),'
            'Es similar a una vista tradicional de Django',
            'Nos da mayor control sobre la logica de nusra aplicacion'
            'Eta mapeado manualmente a los URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """crea un mensaje con suestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message' : message})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put (self, request, pk =None):
        """maneja actualizar un objeto"""
        return Response ({'method' : 'PUT'})

    def patch(request, pk = None):
        """Maneja actualizacion parcial de un objeto"""
        return Response ({'method': 'PATCH'})

    def delete(self, request, pk = None):
        """Borra un Objecto"""
        return Response ({'method': 'DELETE'})
        