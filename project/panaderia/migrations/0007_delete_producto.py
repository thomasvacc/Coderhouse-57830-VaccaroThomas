# Generated by Django 5.1 on 2024-09-24 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panaderia', '0006_remove_producto_categoria'),
        ('pedido', '0004_alter_pedido_servicio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
