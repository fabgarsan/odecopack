# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0041_auto_20170131_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsbiable',
            name='alto',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='ancho',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='categoria_mercadeo_tres',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='diametro',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='dientes',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='linea',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='longitud',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itemsbiable',
            name='serie',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]