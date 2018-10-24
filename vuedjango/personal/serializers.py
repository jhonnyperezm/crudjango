from rest_framework import serializers
from .models import Autor, Choice

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id','documento','nombre','fecha_naci')

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id','titulo','contenido','autor','nombreAutor')