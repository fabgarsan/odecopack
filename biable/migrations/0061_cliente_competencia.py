# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0060_auto_20170207_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='competencia',
            field=models.BooleanField(default=False),
        ),
    ]
