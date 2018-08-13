# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

# Register your models here.

class CiudadInlineAdmin(admin.StackedInline):
    model = models.Ciudad
    extra = 0


class DepartamentoAdmin(admin.ModelAdmin):
    inlines = [CiudadInlineAdmin]
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class LugarInlineAdmin(admin.StackedInline):
    model = models.Lugar
    extra = 0

class ImagenInlineAdmin(admin.StackedInline):
    model = models.ImagenCiudad
    extra = 0

class CiudadAdmin(admin.ModelAdmin):
    inlines = [ImagenInlineAdmin, LugarInlineAdmin]
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class LugarAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class CursoInlineAdmin(admin.StackedInline):
    model = models.Curso
    extra = 0


class PonenteAdmin(admin.ModelAdmin):
    inlines = [CursoInlineAdmin]
    list_display = ['nombre', 'descripcion', 'estado']
    search_fields = ['nombre', 'descripcion']


class CursoAdmin(admin.ModelAdmin):
    list_display = ['ponente', 'nombre', 'descripcion', 'ciudad', 'lugar', 'duracion', 'fecha' ,'inicio', 'fin', 'estado']
    search_fields = ['ponente__nombre', 'ponente__descripcion', 'descripcion', 'ciudad__nombre']


class SuscripcionInlineAdmin(admin.StackedInline):
    model = models.SuscripcionCurso
    extra = 1
#end class


class ClienteAdmin(admin.ModelAdmin):
    inlines = [SuscripcionInlineAdmin]
    list_display = ['nombre', 'apellidos', 'tipo_documento', 'identificacion', 'sexo', 'correo', 'celular', 'telefono', 'ciudad']


class SuscripcionesAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'curso', 'valor', 'valor']


class ImagenCiudadAdmin(admin.ModelAdmin):
    list_display = ['ciudad', 'descripcion', 'estado']

class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'celular', 'direccion', 'mensaje']


admin.site.register(models.Departamento, DepartamentoAdmin)
admin.site.register(models.Ciudad, CiudadAdmin)
admin.site.register(models.Lugar, LugarAdmin)
admin.site.register(models.Ponente, PonenteAdmin)
admin.site.register(models.Curso, CursoAdmin)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.SuscripcionCurso, SuscripcionesAdmin)
admin.site.register(models.ImagenCiudad, ImagenCiudadAdmin)
admin.site.register(models.Configuracion, ConfiguracionAdmin)
