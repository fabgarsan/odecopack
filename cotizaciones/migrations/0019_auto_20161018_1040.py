# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0018_auto_20161018_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareacotizacion',
            name='descripcion',
            field=models.TextField(max_length=300),
        ),
    ]
