from rest_framework import serializers
from pedidos.models import TabelaPedido, Cliente ,Produto

class TabelaPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabelaPedido
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ListaPedidosDoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabelaPedido
        fields = '__all__'

class ClientePorIdClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'