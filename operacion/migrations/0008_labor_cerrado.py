# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0007_remove_configuracion_festivos'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor',
            name='cerrado',
            field=models.BooleanField(default=False),
        ),
    ]