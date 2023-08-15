from django.db import models
from datetime import datetime

class Pedido(models.Model):

    numero_pedido= models.IntegerField(null=False, default=0)
    data_pedido_real = models.DateField(null=False, default="")
    nome = models.CharField(max_length=255, null=False, default="")
    estado = models.CharField(max_length=255, null=False, default="")
    cidade = models.CharField(max_length=255, null=False, default="")
    cep = models.IntegerField(null=True)
    telefone1 = models.IntegerField(null=False, default=0)
    telefone2 = models.IntegerField(null=True)
    email = models.CharField(max_length=255, null=False, default="")
    itens_do_pedido = models.CharField(max_length=500, null=False, default="")
    valor_do_pedido = models.FloatField(null=False, default=0.0)
    status_do_pedido = models.CharField(max_length=50, default="")
    data_ultimo_status = models.DateField(null=False, default="")
    codigo_vendedor = models.CharField(max_length=255, null=False, default="")
    prazo_informado = models.IntegerField(null=False, default=0)
    tipo_de_cliente = models.CharField(max_length=255, null=True)
    data_envio = models.DateField(null=True)
    data_aprovado = models.DateField(null=True)
    data_prevista = models.DateField(null=True)
    cpfcnpj = models.BigIntegerField(null=False , default=0)
    cupom_utilizado = models.CharField(max_length=255, null=False, blank=True)
    qtd_pedido = models.IntegerField(null=False, default=0)
    status_recorrencia = models.CharField(max_length=50, default="")
    id_cliente = models.IntegerField(null=False, default=0)
    boleto = models.CharField(max_length=255, null=True)
    vencimento = models.CharField(max_length=255, null=False, default="")
    endereco_boleto = models.CharField(max_length=255, null=False, default="")
    total_produto = models.FloatField(null=False, default=0.0)
    total_frete = models.FloatField(null=False, default=0.0)
    total_desconto = models.FloatField(null=False,default=0.0)
    forma_pagamento = models.CharField(max_length=50, default="")
    codigo_autorizacao = models.CharField(max_length=50, null=True)
    comentario_aprovado = models.TextField(null=True)
    unidades_vendidas = models.IntegerField(null=True)
    prazo_adicional = models.IntegerField(null=True)

    def __str__(self):
        return self.numero_pedido

from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, default="")
    id_cliente = models.CharField(max_length=255, null=False, default="")
    estado = models.CharField(max_length=255, null=True, default="")
    endereco = models.JSONField(null=True)
    telefone1 = models.CharField(max_length=20)
    telefone2 = models.CharField(max_length=20)
    email = models.CharField(max_length=255, default="")
    cpfcnpj = models.CharField(max_length=20)
    rg_ie = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome}"

class TabelaPedido(models.Model):

    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    numero_pedido= models.IntegerField(null=False, default=0)
    data_pedido_real = models.DateField(null=False, default="")
    nome = models.CharField(max_length=255, null=False, default="")
    estado = models.CharField(max_length=255, null=False, default="")
    cidade = models.CharField(max_length=255, null=False, default="")
    cep = models.CharField(max_length=255, null=True, default="")
    telefone1 = models.CharField(max_length=255, null=False, default="")
    telefone2 = models.CharField(max_length=255, null=True, default="")
    email = models.CharField(max_length=255, null=False, default="")
    itens_do_pedido = models.JSONField(null=True)
    valor_do_pedido = models.FloatField(null=False, default=0.0)
    status_do_pedido = models.CharField(max_length=50, default="")
    data_ultimo_status = models.DateField(null=False, default="")
    codigo_vendedor = models.CharField(max_length=255, null=False, default="")
    prazo_informado = models.IntegerField(null=False, default=0)
    tipo_de_cliente = models.CharField(max_length=255, null=True)
    data_envio = models.DateField(null=True)
    data_aprovado = models.DateField(null=True)
    data_prevista = models.DateField(null=True)
    cpfcnpj = models.CharField(max_length=255, null=False , default=0)
    cupom_utilizado = models.CharField(max_length=255, null=False, blank=True)
    qtd_pedido = models.IntegerField(null=False, default=0)
    status_recorrencia = models.CharField(max_length=50, default="")
    id_cliente = models.CharField(max_length=255, null=False, default=0)
    boleto = models.CharField(max_length=255, null=True)
    vencimento = models.CharField(max_length=255, null=False, default="")
    endereco_boleto = models.CharField(max_length=255, null=False, default="")
    total_produto = models.FloatField(null=False, default=0.0)
    total_frete = models.FloatField(null=False, default=0.0)
    total_desconto = models.FloatField(null=False,default=0.0)
    forma_pagamento = models.CharField(max_length=50, default="")
    codigo_autorizacao = models.CharField(max_length=50, null=True)
    comentario_aprovado = models.TextField(null=True)
    unidades_vendidas = models.IntegerField(null=True)
    prazo_adicional = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.numero_pedido}"

class Produto(models.Model):
    

    isCustomizeable = models.BooleanField(default=True)
    product_id = models.IntegerField()
    product_code = models.CharField(max_length=20, null=True)
    sku_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_name_html = models.CharField(max_length=255)
    product_total = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    product_delivery_time = models.CharField(max_length=255,null=True)
    image = models.URLField()
    brand = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255,null=True, blank=True)
    external_id_product = models.IntegerField(null=True)
    external_id_sku = models.IntegerField(null=True)
    is_kit = models.BooleanField()
    products_kit = models.JSONField(null=True)
    sku_code = models.CharField(max_length=20, null=True)
    product_cross_docking = models.IntegerField()
    attributes = models.JSONField(null=True)
    cubing = models.JSONField(null=True)




    def __str__(self):    
        return f" { self.product_code} {self.product_name}"
    