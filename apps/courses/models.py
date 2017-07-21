# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from organization.models import Teacher, CourseOrg

from DjangoUeditor.models import UEditorField
# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    #detail = UEditorField(verbose_name=u'课程详情',width=600, height=300, imagePath="course/ueditor/", filePath="course/ueditor/",blank=True, default='')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否轮播')
    teacher = models.ForeignKey(Teacher, verbose_name=u'讲师', null=True, blank=True)
    degree = models.CharField(choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')), max_length=5, verbose_name=u'难度')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'封面图')
    category = models.CharField(default=u'后端开发', max_length=30, verbose_name=u'课程类别')
    tag = models.CharField(default='', verbose_name=u'课程标签', max_length=30)
    notice = models.CharField(max_length=400, verbose_name=u'课程须知', default='')
    learn = models.CharField(max_length=300, verbose_name=u'学到什么', default='')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_nums(self):
        return self.lesson_set.all().count()
    get_lesson_nums.short_description = u'章节数'

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程名')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    #获取章节视频
    def get_lesson_video(self):
        return self.video_set.all()

class BannerCourse(Course):
    class Meta:
        verbose_name = u'轮播课程'
        verbose_name_plural = verbose_name
        proxy = True


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节名')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    poster = models.ImageField(verbose_name=u'封面', upload_to='course/poster/%Y/%m', max_length=200, null=True, blank=True)
    url = models.URLField(max_length=300, verbose_name=u'视频地址', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name=u'资源文件', max_length=150)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name