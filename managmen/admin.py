# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

# Register your models here.


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class CiudadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class LugarAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class PonenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class CursoAdmin(admin.ModelAdmin):
    list_display = ['ponente', 'nombre', 'descripcion', 'ciudad', 'lugar', 'duracion', 'fecha' ,'inicio', 'fin', 'estado']
    search_fields = ['ponente__nombre', 'ponente__descripcion', 'descripcion', 'ciudad__nombre']


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'tipo_documento', 'identificacion', 'sexo', 'correo', 'celular', 'telefono', 'ciudad']


admin.site.register(models.Departamento, DepartamentoAdmin)
admin.site.register(models.Ciudad, CiudadAdmin)
admin.site.register(models.Lugar, LugarAdmin)
admin.site.register(models.Ponente, PonenteAdmin)
admin.site.register(models.Curso, CursoAdmin)
admin.site.register(models.Cliente, ClienteAdmin)

