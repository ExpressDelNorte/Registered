from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#empleado
urlpatterns = [
    url(r'^login/empleado/$',login_required(views.LoginEmpleado.as_view()) ,name='login_empleado'),
    url(r'^add/empleado/$',login_required(views.AddEmpleado.as_view()) ,name='add_empleado'),
    url(r'^edit/empleado/(?P<pk>\d+)/$',login_required(views.EditEmpleado.as_view()) ,name='edit_empleado'),
    url(r'^delete/empleado/(?P<pk>\d+)/$',login_required(views.DeleteEmpleado.as_view()) ,name='delete_empleado'),
    url(r'^list/empleado/',login_required(views.ListEmpleado.as_view()) ,name='lis_empleado'),
    url(r'^list/empleados/',login_required(views.ListEmpleados.as_view()) ,name='list_empleados'),
    url(r'^change/pass/empleados/',login_required(views.SetPassWordEmpleado.as_view()) ,name='set_pass_empleado'),
]


#direccionamientos del empleado a nivel de vista
urlpatterns += [
    url(r'^view/empleados/$',login_required(views.GeneralCliente.as_view()), name='view_empleados'),
]
