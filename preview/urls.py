__author__ = 'niels'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='preview'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^createuser/$', views.create_user, name='create_user'),
    url(r'^user/$', views.user_page, name='user_page'),
]