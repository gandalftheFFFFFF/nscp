
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.latest, name='news'),
    url(r'^latest/$', views.latest, name='latest'),
    url(r'^all/$', views.all, name='all'),
]