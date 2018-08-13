# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from managmen import models as managmen

class IndexAdmin(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        return redirect('/admin/')
    # end def
# end class


class LandingView(TemplateView):
    def get(self, request, *args, **kwargs):
        ciudades = managmen.Ciudad.objects.filter(estado=True).order_by('id')
        imagenes = managmen.ImagenCiudad.objects.filter(estado=True).order_by('id')
        activate=imagenes.first() if imagenes.count() else None
        ponentes = managmen.Ponente.objects.filter(estado=True)
        configuracion = managmen.Configuracion.objects.all().first()
        return render(request, 'smart_customer/index.html', {'ciudades': ciudades, 'activate': activate, 'ponentes':ponentes, 'configuracion': configuracion})