# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
import models

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = models.Configuracion
        fields = ['empresa','ordinario','fincho','festivos']
        exclude = ['estado']
    #end class
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
