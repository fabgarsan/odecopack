# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0008_contactoempresa_fecha_cumpleanos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactoempresa',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='contactoempresa',
            name='ciudad_alternativa',
        ),
        migrations.RemoveField(
            model_name='contactoempresa',
            name='nit_alternativo',
        ),
    ]
