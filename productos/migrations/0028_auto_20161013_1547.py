# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0027_producto_rentabilidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': '1. Productos'},
        ),
        migrations.AlterModelOptions(
            name='unidadmedida',
            options={'verbose_name_plural': '2. Unidades de Medida'},
        ),
    ]
