from django.shortcuts import render
from rest_framework import viewsets, generics
from pedidos.models import TabelaPedido, Cliente, Produto
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from pedidos.serializer import TabelaPedidoSerializer, ClienteSerializer, ListaPedidosDoClienteSerializer, ClientePorIdClienteSerializer, ProdutoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

class CustomPagination(PageNumberPagination):

    page_size_query_param = 'page_size'  


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = TabelaPedido.objects.all()
    serializer_class = TabelaPedidoSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'update']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'update']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class PedidoPorNumeroPedidoViewSet(generics.RetrieveUpdateDestroyAPIView):
    """Lista pedido com base no numero do pedido"""
    queryset = TabelaPedido.objects.all()
    serializer_class = TabelaPedidoSerializer
    lookup_field = 'numero_pedido'  
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['nome', 'cpf']
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class ListaPedidosDoCliente(generics.ListAPIView):
    """Lista os pedidos do cliente com base no id_cliente"""
    serializer_class = ListaPedidosDoClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = TabelaPedido.objects.filter(id_cliente=self.kwargs['id_cliente'])
        return queryset

class ClientePorId_clienteViewSet(generics.RetrieveUpdateDestroyAPIView):
    """Lista cliente com base no id_cliente"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = 'id_cliente'  
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ClientePorLocalizacaoViewSet(generics.ListAPIView):
    """Retorna clientes com base em sua localização"""
    serializer_class = ClientePorIdClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Cliente.objects.filter(endereco__state=self.kwargs['UF'])
        return queryset
    
 
