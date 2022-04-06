from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ serializa un ampo para probar nuestro APIView"""
    name = serializers.CharField(max_length=10)