from django.conf.urls import patterns, url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'login/$', views.custom_login, {'template_name': 'usuario/login.html'}, name='user-login'),
    url(r'logout/$', views.custom_logout, {'next_page': '/', }, name='user-logout'),
]
