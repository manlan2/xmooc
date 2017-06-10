# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from . import views
from users.views import LoginView, RegisterView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^usercenter_info/$', views.usercenter_info, name='usercenter_info'),
    url(r'^usercenter_mycourse/$', views.usercenter_mycourse, name='usercenter_mycourse'),
    url(r'^usercenter_mystore/$', views.usercenter_mystore, name='usercenter_mystore'),
    url(r'^usercenter_mymessage/$', views.usercenter_mymessage, name='usercenter_mymessage'),
]