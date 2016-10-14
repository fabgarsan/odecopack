# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_auto_20161010_1021'),
        ('proveedores', '0010_proveedor_factor_importacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='MargenProvedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('margen_deseado', models.DecimalField(decimal_places=3, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='margenes_por_proveedor', to='productos.CategoriaMargen')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_margenes_categoria', to='proveedores.Proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='proveedor',
            name='margenes',
            field=models.ManyToManyField(through='proveedores.MargenProvedor', to='productos.CategoriaMargen'),
        ),
    ]