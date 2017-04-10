# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import forms
from django.contrib import admin
import models


class LaborAdmin(admin.ModelAdmin):
    list_display = ['empleado','fin']
    form = forms.LaborForm
#end class


class DiaAdmin(admin.ModelAdmin):
    list_display = ['year','dia']
    form = forms.DiaForm
#end class


class CalendarioAdmin(admin.ModelAdmin):
    list_display = ['dia']
    form = forms.CalendarioForm
#end class


class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ['empresa','ordinario','fincho']
    form = forms.ConfiguracionForm
#end class

# Register your models here.
admin.site.register(models.Configuracion, ConfiguracionAdmin)
admin.site.register(models.Calendario, CalendarioAdmin)
admin.site.register(models.Dia, DiaAdmin)
admin.site.register(models.Labor, LaborAdmin)
