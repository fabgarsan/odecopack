# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos_caracteristicas', '0001_initial'),
        ('productos', '0007_articulocatalogo_id_cguno'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='articulocatalogo',
            unique_together=set([('referencia', 'fabricante')]),
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=set([('referencia', 'fabricante')]),
        ),
    ]