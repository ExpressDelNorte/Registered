# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 19:11
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='empresa',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='first_name',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='username',
        ),
        migrations.AddField(
            model_name='empresa',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]