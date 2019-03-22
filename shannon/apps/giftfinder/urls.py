from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^dashboard/$', views.dashboard),
    url(r'^logout/$', views.logout),
    url(r'^addjob/$', views.addjob),
    url(r'^submit/$', views.jobadd),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^edit/(?P<id>\d+)/submit/$', views.editsubmit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^join/(?P<id>\d+)/$', views.join),
    # url(r'^cancel/(?P<id>\d+)/$', views.cancel),
]