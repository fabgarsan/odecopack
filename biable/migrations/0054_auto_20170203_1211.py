# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-03 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0053_auto_20170203_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientoventabiable',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='movimientoventabiable',
            name='day',
        ),
        migrations.RemoveField(
            model_name='movimientoventabiable',
            name='id_terc_fa',
        ),
        migrations.RemoveField(
            model_name='movimientoventabiable',
            name='month',
        ),
        migrations.RemoveField(
            model_name='movimientoventabiable',
            name='vendedor',
        ),
        migrations.RemoveField(
            model_name='movimientoventabiable',
            name='year',
        ),
    ]
