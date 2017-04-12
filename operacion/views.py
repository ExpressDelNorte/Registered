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
from cuser.middleware import CuserMiddleware
from django.views.generic import View, DeleteView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, get_object_or_404, HttpResponse
from empresa import models as empresa
from django.utils import timezone


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


class ListConfiguracion(supra.SupraListView):
    model = models.Configuracion
    search_key = 'q'
    list_display = ['id','ordinario','fincho']
    search_fields = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ListConfiguracion, self).get_queryset()
        user = CuserMiddleware.get_user()
        confi = models.Configuracion.objects.filter(empresa__tienda__empleado__user_ptr_id=user.id,estado=True)
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListConfiguracion, self).dispatch(*args, **kwargs)
    # end def
# end class


class AddLabor(supra.SupraFormView):
    model = models.Labor
    form_class = forms.LaborFormView
    template_name = 'operacion/addlabor.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddLabor, self).dispatch(*args, **kwargs)
    # end def
# end class


class ListLabor(supra.SupraListView):
    model = models.Labor
    search_key = 'q'
    list_display = ['id','empleado','ini']
    search_fields = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ListLabor, self).get_queryset()
        user = CuserMiddleware.get_user()
        tienda = empresa.Tienda.objects.filter(empleado__user_ptr_id=user.id).first()
        print tienda
        confi = models.Labor.objects.filter(empleado__tienda=tienda,estado=True,cerrado=False)
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListLabor, self).dispatch(*args, **kwargs)
    # end def
# end class


class LoginEmpleado(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(LoginEmpleado, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        username = request.GET.get('user', False)
        passw = request.GET.get('pass', False)
        if username and passw:
            user = authenticate(username=username, password=passw)
            if user is not None:
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
        # end if
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class


class EditLabor(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(EditLabor, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        print request,kwargs
        labor=kwargs['pk']
        empleado = request.GET.get('empleado', False)
        if labor:
            print 1
            lab = models.Labor.objects.filter(id=labor).first()
            if lab:
                print 2
                lab.cerrado=True
                lab.fin = timezone.now()
                lab.save()
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
        # end if
        print 3
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class
