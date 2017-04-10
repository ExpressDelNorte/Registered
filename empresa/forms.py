# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
import models

class CiudadForm(forms.ModelForm):
    class Meta:
        model = models.Ciudad
        fields = ['nombre']
        exclude = ['status']
    #end class
#end class


class EmpresaForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Empresa
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
         'nit', 'direccion','celular', 'telefono', 'ciudad', 'logo']
        exclude = ['last_name']
    # end class
#end class


class EmpresaEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmpresaEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Empresa
        fields = ['username','email', 'first_name',
         'nit', 'direccion','celular', 'telefono', 'ciudad', 'logo']
        exclude = ['last_name', 'password1', 'password2',]
    # end class
#end class

class TiendaForm(forms.ModelForm):
    class Meta:
        model = models.Tienda
        fields = ['empresa','ciudad','nombre','direccion','referencia','fijo','celular']
        exclude = ['status']
    #end class
#end class
