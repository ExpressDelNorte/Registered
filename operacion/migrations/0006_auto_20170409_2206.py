# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0005_auto_20170409_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labor',
            name='ini',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
