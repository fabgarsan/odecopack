# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0039_auto_20170308_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='contacto_nuevo',
            field=models.BooleanField(default=False),
        ),
    ]