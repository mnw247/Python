from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.register),
    url(r'^login$',views.login),
    url(r'^books$', views.books),
    url(r'^books/add$', views.addbooks),
    url(r'^books/(?P<id>\d+)$',views.book_view),
    url(r'^users/(?P<id>\d+)$',views.user_view),
    url(r'^users/(?P<id>\d+)/delete$', views.destroy),
    url(r'^logout$', views.logout_view),
]
