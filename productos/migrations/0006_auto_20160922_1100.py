# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_delete_habitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_cguno',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
