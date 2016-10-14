# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0012_auto_20161010_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='margenprovedor',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='margenes_por_proveedor', to='listasprecios.CategoriaMargen'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='margenes',
            field=models.ManyToManyField(through='proveedores.MargenProvedor', to='listasprecios.CategoriaMargen'),
        ),
    ]