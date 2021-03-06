# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biable', '0020_auto_20161228_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartera',
            options={'permissions': (('ver_carteras', 'R Cart. Vcto'), ('ver_carteras_todos', 'R Cart. Vcto Todos'))},
        ),
        migrations.AlterField(
            model_name='vendedorbiableuser',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_vendedores', to='usuarios.UserExtended', unique=True),
        ),
    ]
