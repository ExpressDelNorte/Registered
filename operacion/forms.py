# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
import models
from cuser.middleware import CuserMiddleware
from usuario import models as usuario

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = models.Configuracion
        fields = ['empresa','ordinario','fincho']
        exclude = ['estado']
    #end class
#end class


class ConfiguracionFormView(forms.ModelForm):
    class Meta:
        model = models.Configuracion
        fields = ['ordinario','fincho']
        exclude = ['estado']
    #end class

    def save(self, commit):
		obj = super(ConfiguracionFormView, self).save(commit)
        empresa = Empresa.objects.filter(id=1)
		obj.empresa = None
		return obj
	#end def
#end class


class CalendarioForm(forms.ModelForm):
    class Meta:
        model = models.Calendario
        fields = ['year']
        exclude = ['estado']
    #end class
#end class


class DiaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiaForm, self).__init__(*args, **kwargs)
        self.fields['dia'].widget = widgets.AdminDateWidget()
    # end def

    class Meta:
        model = models.Dia
        fields = ['year','dia']
        exclude = ['estado']
    #end class
#end class


class LaborForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LaborForm, self).__init__(*args, **kwargs)
        self.fields['ini'].widget = widgets.AdminSplitDateTime()
        self.fields['fin'].widget = widgets.AdminSplitDateTime()
    # end def

    class Meta:
        model = models.Labor
        fields = ['empleado','ini','fin']
        exclude = ['estado']
    #end class
#end class



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
