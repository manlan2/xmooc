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
	url(r'^org-courses/(?P<org_id>[0-9]+)$', views.org_courses, name='org-courses'),
	url(r'^org-desc/(?P<org_id>[0-9]+)$', views.org_desc, name='org-desc'),
	url(r'^org-teachers/(?P<org_id>[0-9]+)$', views.org_teachers, name='org-teachers'),
    url(r'teacher/detail/(?P<teacher_id>[0-9]+)$', views.detail, name='detail'),
]