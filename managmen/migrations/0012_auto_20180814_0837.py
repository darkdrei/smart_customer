# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-14 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managmen', '0011_configuracion_mensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='duracion',
        ),
        migrations.AddField(
            model_name='curso',
            name='url_pago',
            field=models.CharField(default=1, max_length=1000, verbose_name='Link de pago'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='celular',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='correo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='direccion',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='mensaje',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Te contactaremos.'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='nombre',
            field=models.CharField(blank=True, default='Express del norte', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(max_length=1000, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='imagenciudad',
            name='descripcion',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='imagenciudad',
            name='titulo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='ponente',
            name='descripcion',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='Descripci\xf2n'),
        ),
        migrations.AlterField(
            model_name='ponente',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
    ]