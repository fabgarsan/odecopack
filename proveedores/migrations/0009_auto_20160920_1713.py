# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0008_auto_20160920_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='importaciones.Moneda'),
        ),
        migrations.DeleteModel(
            name='Moneda',
        ),
    ]