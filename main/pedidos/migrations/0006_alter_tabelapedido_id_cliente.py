# Generated by Django 4.2.4 on 2023-08-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_alter_tabelapedido_cpfcnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelapedido',
            name='id_cliente',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
