# Generated by Django 4.2.4 on 2023-08-07 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_alter_tabelapedido_itens_do_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255)),
                ('id_cliente', models.CharField(default='', max_length=255)),
                ('estado', models.CharField(default='', max_length=255, null=True)),
                ('endereco', models.JSONField(null=True)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
                ('cpfcnpj', models.CharField(max_length=20)),
                ('rg_ie', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='tabelapedido',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.cliente'),
        ),
    ]
