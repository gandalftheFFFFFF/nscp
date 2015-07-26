
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^post/(.*)', views.specific_post, name='specific_post'),
    url(r'^archive/$', views.archive, name='archive'),
]
