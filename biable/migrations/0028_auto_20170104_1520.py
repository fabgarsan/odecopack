# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-04 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('biable', '0027_auto_20170104_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineavendedorbiable',
            name='colaborador',
        ),
        migrations.AddField(
            model_name='vendedorbiable',
            name='colaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mi_vendedor_biable', to='usuarios.UserExtended'),
        ),
    ]
