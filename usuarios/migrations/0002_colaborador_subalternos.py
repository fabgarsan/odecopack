# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-04 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='subalternos',
            field=models.ManyToManyField(related_name='_colaborador_subalternos_+', to='usuarios.Colaborador'),
        ),
    ]