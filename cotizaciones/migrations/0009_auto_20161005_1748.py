# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0008_cotizacion_fecha_envio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha_envio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
