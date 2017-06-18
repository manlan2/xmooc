# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from courses.views import CommentView, AddCommentsView, VideoPlayView

urlpatterns = [
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^course_detail/(?P<course_id>[0-9]*)$', views.course_detail, name='course_detail'),
    url(r'^course/lesson/(?P<course_id>[0-9]*)$', views.lesson, name='lesson'),
    url(r'^comment/(?P<course_id>[0-9]*)$', CommentView.as_view(), name='comment'),
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
    url(r'^video/(?P<video_id>\d+)$', VideoPlayView.as_view(), name='video_play'),
]