# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from supra import views as supra
import forms
import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
class AddConfiguracion(supra.SupraFormView):
    model = models.Configuracion
    form_class = forms.ConfiguracionFormView
    template_name = 'operacion/addconfig.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddConfiguracion, self).dispatch(*args, **kwargs)
    # end def
# end class
