# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0077_seguimientocliente_creado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimientocliente',
            name='tipo',
            field=models.CharField(choices=[('Llamada', 'Llamada'), ('Visita', 'Visita'), ('Envío Correo', 'Envío Correo')], max_length=20),
        ),
    ]
