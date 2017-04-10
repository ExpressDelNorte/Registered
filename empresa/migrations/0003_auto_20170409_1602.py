# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20170409_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='web',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='nit',
        ),
        migrations.AddField(
            model_name='empresa',
            name='celular',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]