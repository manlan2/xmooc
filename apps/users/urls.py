# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from . import views
from users.views import LoginView, RegisterView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^usercenter_info/(?P<user_id>[0-9]+)$', views.usercenter_info, name='usercenter_info'),
    url(r'^usercenter_mycourse/(?P<user_id>[0-9]+)$', views.usercenter_mycourse, name='usercenter_mycourse'),
    url(r'^usercenter_mystore/(?P<user_id>[0-9]+)$', views.usercenter_mystore, name='usercenter_mystore'),
    url(r'^usercenter_mymessage/(?P<user_id>[0-9]+)$', views.usercenter_mymessage, name='usercenter_mymessage'),
]