# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^course/comment/(?P<course_id>[0-9]+)$', views.comment, name='comment'),
    url(r'^addstore/$', views.addstore, name='addstore'),
]