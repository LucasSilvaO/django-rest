# Generated by Django 4.2.4 on 2023-08-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_tabelapedido_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelapedido',
            name='telefone1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='tabelapedido',
            name='telefone2',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]