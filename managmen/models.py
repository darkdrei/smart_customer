# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
MESES = {
    '1': 'Enero',
    '2': 'Febrero',
    '3': 'Marzo',
    '4': 'Abril',
    '5': 'Mayo',
    '6': 'Junio',
    '7': 'Julio',
    '8': 'Agosto',
    '9': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre',
}

class Departamento(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50, verbose_name="Descripciòn", null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Departamentos"
        verbose_name = "Departamento"

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def __str__(self):
        return '{}'.format(self.nombre)



class Ciudad(models.Model):
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50, verbose_name="Descripciòn", null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Ciudades"
        verbose_name = "Ciudad"

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def __str__(self):
        return '{}'.format(self.nombre)


class ImagenCiudad(models.Model):
    ciudad = models.ForeignKey(Ciudad)
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(max_length=400, blank=True, null=True)
    imagen = models.ImageField(upload_to= 'ciudad/', null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Fotos de ciudad"
        verbose_name = "Foto ciudad"

    def __unicode__(self):
        return '{}'.format(self.ciudad.nombre)

    def __str__(self):
        return '{}'.format(self.ciudad.nombre)



class Lugar(models.Model):
    ciudad = models.ForeignKey(Ciudad)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50, verbose_name="Descripciòn", null=True, blank=True)
    imagen = models.ImageField(upload_to='lugar/', null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Lugares"
        verbose_name = "Lugar"

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def __str__(self):
        return '{}'.format(self.nombre)



class Ponente(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50, verbose_name="Descripciòn", null=True, blank=True)
    imagen = models.ImageField(upload_to='lugar/', null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Ponentes"
        verbose_name = "Ponente"

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def __str__(self):
        return '{}'.format(self.nombre)


class Curso(models.Model):
    ponente = models.ForeignKey(Ponente)
    imagen = models.ImageField(upload_to='media/curso/', null=True, blank=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50, verbose_name="Descripciòn")
    precio = models.FloatField(default=0)
    ciudad = models.ForeignKey(Ciudad)
    lugar = models.ForeignKey(Lugar)
    duracion = models.FloatField(verbose_name="Duracion en meses")
    fecha = models.DateField(verbose_name="Fecha de realizacion", blank=True)
    inicio=models.TimeField(verbose_name="Hora de inicio", blank=True)
    fin=models.TimeField(verbose_name="Hora de fin", blank=True)
    activo = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)

    def get_inicio(self):
        return '{} {} {}'.format(self.fecha.day, MESES.get(str(self.fecha.month)), self.fecha.year)

    def get_hora(self):
        return '{}-{}'.format(self.get_change_hour(self.inicio), self.get_change_hour(self.fin))

    def get_change_hour(self, hora):
        if hora:
            cardinalidad = 'Pm' if hora.hour >= 12 else 'Am'
            return '{}:{}{}'.format(hora.hour if hora.hour <= 12 else hora.hour - 12, hora.minute, cardinalidad)
        return ""

    class Meta:
        verbose_name_plural = "Cursos"
        verbose_name = "Curso"

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def __str__(self):
        return '{}'.format(self.nombre)


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    nacimiento = models.DateField(blank=True)
    tipo_documento = models.IntegerField(choices=((1, 'Cédula de Ciudadanía'), (2, 'Tarjeta de Identidad'),
                                                  (3, 'Tarjeta Pasaporte'), (4,'Cédula de Extranjería'),
                                                  (5, 'Pasaporte')), verbose_name="Tipo de documento")
    identificacion = models.CharField(verbose_name="Numero de identificacìon", max_length=20)
    sexo = models.IntegerField(choices=((1, 'Masculino'), (2, 'Femenino')))
    correo = models.EmailField(blank=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    def __unicode__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class SuscripcionCurso(models.Model):
    cliente = models.ForeignKey(Cliente)
    curso = models.ForeignKey(Curso)
    paga = models.BooleanField(default=False)
    valor = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "Suscripciones curso"
        verbose_name = "Suscripcion curso"

    def __unicode__(self):
        return '{} {} -- {}'.format(self.cliente.nombre if self.cliente else '',
                                    self.clienteapellidos if self.cliente else '',
                                    self.curso.nombre if self.curso else '')

    def __str__(self):
        return '{} {} -- {}'.format(self.cliente.nombre if self.cliente else '',
                                    self.clienteapellidos if self.cliente else '',
                                    self.curso.nombre if self.curso else '')

class Configuracion(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True, default='Express del norte')
    correo = models.CharField(max_length=30, null=True, blank=True)
    celular = models.CharField(max_length=30, null=True, blank=True)
    direccion = models.CharField(max_length=30, null=True, blank=True, verbose_name='Dirección')
    mensaje = models.CharField(max_length=30, null=True, blank=True, verbose_name='Te contactaremos.')

    class Meta:
        verbose_name_plural = "Configuraciones"
        verbose_name = "Configuracion"

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def __str__(self):
        return '{}'.format(self.nombre)