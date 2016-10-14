# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0023_auto_20161010_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='costo_base',
            new_name='costo_cop',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_base',
            field=models.DecimalField(decimal_places=4, default=0, editable=False, max_digits=18),
        ),
    ]