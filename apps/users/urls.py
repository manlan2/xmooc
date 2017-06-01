from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.userlogin, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^orgs/$', views.orgs, name='orgs'),
    url(r'^usercenter_info/$', views.usercenter_info, name='usercenter_info'),
    url(r'^usercenter_mycourse/$', views.usercenter_mycourse, name='usercenter_mycourse'),
    url(r'^usercenter_mystore/$', views.usercenter_mystore, name='usercenter_mystore'),
    url(r'^usercenter_mymessage/$', views.usercenter_mymessage, name='usercenter_mymessage'),
]