# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listasprecios', '0012_auto_20161007_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listaprecio',
            name='en_lista_precios',
        ),
    ]
