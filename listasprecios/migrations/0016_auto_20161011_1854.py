# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listasprecios', '0015_auto_20161010_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriamargen',
            options={'verbose_name_plural': '3. Margenes x Categoría'},
        ),
        migrations.AlterModelOptions(
            name='formapago',
            options={'verbose_name_plural': '1. Formas de Pago'},
        ),
        migrations.AlterModelOptions(
            name='variablelistaprecio',
            options={'verbose_name_plural': '2. Formas de Pago % sobre precio '},
        ),
        migrations.AddField(
            model_name='formapago',
            name='porcentaje',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=18, verbose_name='%'),
        ),
        migrations.AlterField(
            model_name='variablelistaprecio',
            name='value',
            field=models.DecimalField(decimal_places=3, max_digits=18, verbose_name='%'),
        ),
    ]