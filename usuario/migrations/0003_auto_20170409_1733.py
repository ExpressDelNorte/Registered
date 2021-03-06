# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 22:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_cargo_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='documeno',
        ),
        migrations.AddField(
            model_name='usuario',
            name='documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuario.Documento', verbose_name='Tipo de documento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_celular',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'telefono no valido', 'invalid')], verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_fijo',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'telefono no valido', 'invalid')], verbose_name='Telefono fijo'),
        ),
    ]
