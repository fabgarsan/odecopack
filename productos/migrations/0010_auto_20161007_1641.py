# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_auto_20161006_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='activo_ensamble',
            field=models.BooleanField(default=False),
        ),
    ]
