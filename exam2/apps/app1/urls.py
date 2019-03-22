from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^dashboard/$', views.dashboard),
    url(r'^logout/$', views.logout),
    url(r'^addquote/$', views.addquote),
    url(r'^myaccount/(?P<id>\d+)$', views.accountupdate),
    url(r'^myaccount/(?P<id>\d+)/update/$', views.submitupdate),
    url(r'^user/(?P<id>\d+)$', views.userquotes),
    url(r'^like/(?P<id>\d+)$', views.likedquotes),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]