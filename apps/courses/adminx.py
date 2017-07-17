# -*- coding:utf-8 -*-

import xadmin
from .models import Course, Lesson, Video, CourseResource


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseresourceInline(object):
    model = CourseResource
    extra = 0

class CourseAdmin(object):
    list_display = ('id', 'name', 'desc', 'detail', 'degree', 'learn_times','students','image','add_time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'degree')
    list_filter = ('name', 'degree', 'students', 'add_time', 'click_nums')
    readonly_fields = ('fav_nums', 'click_nums')
    exclude = ('fav_nums',)
    inlines = [LessonInline, CourseresourceInline]

class LessonAdmin(object):
    list_display = ('id', 'course', 'name','add_time')
    list_display_links = ('id', 'name')
    search_fields = ('course', 'name')
    list_filter = ('course__name', 'name', 'add_time')


class VideoAdmin(object):
    list_display = ('id', 'lesson', 'name', 'add_time')
    list_display_links = ('id', 'name')
    search_fields = ('lesson', 'name')
    list_filter = ('lesson__name', 'name', 'add_time')


class CourseresourceAdmin(object):
    list_display = ('id', 'course', 'name', 'download', 'add_time')
    list_display_links = ('id', 'name')
    search_fields = ('course', 'name')
    list_filter = ('course__name', 'name', 'add_time')

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseresourceAdmin)