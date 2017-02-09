# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0030_auto_20170208_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remisioncotizacion',
            name='factura_biable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mis_remisiones', to='biable.FacturasBiable'),
        ),
    ]
