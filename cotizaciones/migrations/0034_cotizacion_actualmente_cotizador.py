# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0033_auto_20170210_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='actualmente_cotizador',
            field=models.BooleanField(default=False),
        ),
    ]