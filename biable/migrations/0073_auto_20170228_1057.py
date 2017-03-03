# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0072_auto_20170228_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguimientocliente',
            name='hora_final',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seguimientocliente',
            name='hora_inicial',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seguimientocliente',
            name='fecha_seguimiento',
            field=models.DateField(),
        ),
    ]