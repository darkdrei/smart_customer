# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managmen', '0010_configuracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='mensaje',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Te contactaremos.'),
        ),
    ]