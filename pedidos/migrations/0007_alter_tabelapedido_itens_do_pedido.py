# Generated by Django 4.2.4 on 2023-08-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_alter_tabelapedido_id_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelapedido',
            name='itens_do_pedido',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
