# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0028_auto_20161010_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='activo_catalogo',
            field=models.BooleanField(default=False, verbose_name='En Cata.'),
        ),
        migrations.AddField(
            model_name='banda',
            name='activo_componentes',
            field=models.BooleanField(default=False, verbose_name='En Compo.'),
        ),
        migrations.AddField(
            model_name='banda',
            name='activo_proyectos',
            field=models.BooleanField(default=False, verbose_name='En Proy.'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='longitud',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Longitud (m)'),
        ),
    ]