# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0040_auto_20170120_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsbiable',
            name='categoria_mercadeo',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='categoria_mercadeo_dos',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
