from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

'''urlpatterns = [
    url(r'login/$', views.custom_login, {'template_name': 'usuario/login.html'}, name='user-login'),
    url(r'logout/$', views.custom_logout, {'next_page': '/', }, name='user-logout'),
]'''

#formularios

urlpatterns = [
    url(r'add/configuracion/$',login_required(views.AddConfiguracion.as_view()) ,name='add-conf'),
]
