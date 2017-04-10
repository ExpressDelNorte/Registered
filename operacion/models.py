# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from empresa import models as empresa
from usuario import models as usuario

# Create your models here.
class Configuracion(models.Model):
    empresa = models.ForeignKey(empresa.Empresa)
    ordinario = models.FloatField()
    fincho = models.FloatField()
    festivos = models.FloatField()
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s'%self.empresa.first_name
    # end def

    def __unicode__(self):
        return u'%s'%self.empresa.first_name
    # end def

    class Meta:
        verbose_name ='Configuracion'
        verbose_name_plural ='Configuraciones'
    #end class
#end class


class Calendario(models.Model):
    year = models.IntegerField(verbose_name='Año')
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%d'%self.year
    # end class

    def __str__(self):
        return u'%d'%self.year
    # end class

    class Meta:
        verbose_name ='Calendario'
        verbose_name_plural ='Calendarios'
    #end class
#end class


class Dia(models.Model):
    year = models.ForeignKey(Calendario)
    dia = models.DateField()
    estado= models.BooleanField(default=True)

    def __unicode__(self):
        return u'%d-%d-%d'%(self.dia.day,self.dia.month,self.dia.year)
    # end class

    def __str__(self):
        return u'%d-%d-%d'%(self.dia.day,self.dia.month,self.dia.year)
    # end class

    class Meta:
        verbose_name ='Dia'
        verbose_name_plural ='Dias'
    #end class
#end class


class Labor(models.Model):
    empleado = models.ForeignKey(usuario.Empleado)
    ini = models.DateTimeField(blank=True,null=True, editable=True)
    fin = models.DateTimeField(blank=True,null=True)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s %s'%(self.empleado.first_name,self.empleado.last_name)
    # end class

    def __str__(self):
        return u'%s %s'%(self.empleado.first_name,self.empleado.last_name)
    # end class

    class Meta:
        verbose_name ='Labor'
        verbose_name_plural ='Labores'
    #end class
#end class
