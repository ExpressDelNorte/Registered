# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('usuario', '0001_initial'),
        ('operacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Empleado'),
        ),
        migrations.AddField(
            model_name='dia',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacion.Calendario'),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa'),
        ),
    ]