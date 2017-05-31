# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime

from courses.models import Course
from users.models import UserProfile

# Create your models here.


class UserQsts(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'电话')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程咨询'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    comments = models.CharField(max_length=300, verbose_name=u'评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'评论时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class UserStore(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    store_id = models.IntegerField(default=0, verbose_name=u'类型id')
    store_type = models.IntegerField(choices=((1,u'课程'),(2,u'课程机构'),(3,u'讲师')), default=1, verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'收藏时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'用户类型')
    message = models.CharField(max_length=600, verbose_name=u'内容')
    is_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.message


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'课程时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user