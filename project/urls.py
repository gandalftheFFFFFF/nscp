
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.projects, name='projects'),
    url(r'^project/(.*)/$', views.specific_project, name='specific_project'),
    url(r'^archive/$', views.projects_archive, name='projects_archive'),
]