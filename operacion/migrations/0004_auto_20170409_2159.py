# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 02:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0003_auto_20170409_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labor',
            old_name='inicio',
            new_name='ini',
        ),
    ]