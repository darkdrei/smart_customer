# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managmen', '0003_auto_20180811_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='descripcion',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='descripcion',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='ponente',
            name='descripcion',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Descripci\xf2n'),
        ),
    ]
