# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
import re
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre
    # end def

    def __str__(self):
        return self.nombre
    # end def
# end class


class Empresa(User):
    nit = models.CharField(max_length=50, validators=[validators.RegexValidator(
        re.compile('^[0-9]+$'), ('numero no valida'))])
    logo = models.ImageField(upload_to='logos_empresas/', null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    celular = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
    #end def

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
# end clas


class Tienda(models.Model):
    empresa = models.ForeignKey(Empresa)
    ciudad = models.ForeignKey(Ciudad)
    nombre = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    fijo = models.CharField(
        max_length=10, verbose_name="Telefono Fijo", null=True, blank=True)
    celular = models.CharField(
        max_length=10, verbose_name="Telefono Celular", null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    # end def
# end class
