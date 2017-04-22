# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_administrador'),
        ('empresa', '0006_supervisor_identificacion'),
    ]

    operations = [
       migrations.AlterModelOptions(
            name='supervisor',
            options={'verbose_name': 'Administrador', 'verbose_name_plural': 'Administradores'},
        ),
        migrations.AddField(
            model_name='supervisor',
            name='empresas',
            field=models.ManyToManyField(to='empresa.Empresa'),
        ),
    ]
