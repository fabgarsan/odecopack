# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0021_auto_20161007_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='empujador',
            field=models.BooleanField(default=False),
        ),
    ]
