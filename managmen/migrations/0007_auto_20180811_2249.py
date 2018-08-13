# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managmen', '0006_imagenciudad_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/curso/'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/lugar/'),
        ),
        migrations.AlterField(
            model_name='ponente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/lugar/'),
        ),
    ]
