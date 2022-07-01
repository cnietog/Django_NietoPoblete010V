from rest_framework import serializers
from Jardineria.models import Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre','perfil','rut','email','direccion','comuna','region','telefono']
