# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.static import serve
from xmooc.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^orgs/$', views.orgs, name='orgs'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'^org-home/(?P<org_id>[0-9]+)$', views.home, name='home'),
]