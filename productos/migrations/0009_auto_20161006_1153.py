# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 16:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0008_auto_20161004_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='activo_componentes',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='activo_ensamble',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='activo_proyectos',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad_minima_venta',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='producto',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='producto',
            name='serie',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='producto',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
