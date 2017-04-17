from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

'''urlpatterns = [
    url(r'login/$', views.custom_login, {'template_name': 'usuario/login.html'}, name='user-login'),
    url(r'logout/$', views.custom_logout, {'next_page': '/', }, name='user-logout'),
]'''

#formularios configuracion
urlpatterns = [
    url(r'add/configuracion/$',login_required(views.AddConfiguracion.as_view()) ,name='add-conf'),
    url(r'edit/configuracion/(?P<pk>\d)/$',login_required(views.AddConfiguracion.as_view()) ,name='add-conf'),
    url(r'list/configuracion/$',login_required(views.ListConfiguracion.as_view()) ,name='add-conf'),
]


#formularios configuracion
urlpatterns += [
    url(r'add/labor/$',login_required(views.AddLabor.as_view()) ,name='add_labor'),
    url(r'edit/labor/(?P<pk>\d)/$',login_required(views.EditLabor.as_view()) ,name='edit_labor'),
    url(r'delete/labor/(?P<pk>\d)/$',login_required(views.DeleteLabor.as_view()) ,name='delete_labor'),
    url(r'list/labor/$',login_required(views.ListLabor.as_view()) ,name='list_labor'),
]
