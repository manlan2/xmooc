# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^orgs/$', views.orgs, name='orgs'),
]