# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0065_cliente_cerro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('ver_clientes', 'Ver Clientes'),), 'verbose_name': 'Cliente', 'verbose_name_plural': 'C-1.1 Clientes'},
        ),
    ]
