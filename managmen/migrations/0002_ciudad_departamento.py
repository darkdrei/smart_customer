# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managmen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='managmen.Departamento'),
            preserve_default=False,
        ),
    ]
