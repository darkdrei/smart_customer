# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managmen', '0002_ciudad_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenCiudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=400, null=True)),
                ('imagen', models.ImageField(default='', upload_to='ciudad/')),
                ('estado', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managmen.Ciudad')),
            ],
            options={
                'verbose_name': 'Foto ciudad',
                'verbose_name_plural': 'Fotos de ciudad',
            },
        ),
        migrations.CreateModel(
            name='SuscripcionCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paga', models.BooleanField(default=False)),
                ('valor', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Suscripcion curso',
                'verbose_name_plural': 'Suscripciones curso',
            },
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='ponente',
            options={'verbose_name': 'Ponente', 'verbose_name_plural': 'Ponentes'},
        ),
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(default='', upload_to='curso/'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='ciudad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='managmen.Ciudad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lugar',
            name='imagen',
            field=models.ImageField(default='', upload_to='lugar/'),
        ),
        migrations.AddField(
            model_name='ponente',
            name='imagen',
            field=models.ImageField(default='', upload_to='lugar/'),
        ),
        migrations.AddField(
            model_name='suscripcioncurso',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managmen.Cliente'),
        ),
        migrations.AddField(
            model_name='suscripcioncurso',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managmen.Curso'),
        ),
    ]
