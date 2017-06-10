# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^courses/$', views.courses, name='courses'),
	url(r'^course_detail/(?P<course_id>[0-9]+)$', views.course_detail, name='course_detail'),
	url(r'^course/lesson/(?P<course_id>[0-9]+)$', views.lesson, name='lesson'),
]