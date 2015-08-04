__author__ = 'niels'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='preview'),
    url(r'^login/$', views.log_in, name='login'),
]