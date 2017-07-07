# -*- coding:utf-8 -*-

import xadmin
from .models import UserQsts, CourseComments, UserStore, UserMessage, UserCourse


class UserQstsAdmin(object):
    list_display = ('id', 'name', 'mobile', 'course_name', 'add_time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'course_name')
    list_filter = ('name', 'course_name', 'add_time')
    model_icon = 'fa fa-question'



class CourseCommentsAdmin(object):
    list_display = ('id', 'user', 'course','comments', 'add_time')
    list_display_links = ('id', 'course')
    search_fields = ('user', 'course', 'comments')
    list_filter = ('user__username', 'course__name', 'comments', 'add_time')
    model_icon = 'fa fa-comments'

class UserStoreAdmin(object):
    list_display = ('id', 'user', 'store_id','store_type', 'add_time')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'store_id', 'store_type')
    list_filter = ('user__username', 'store_id', 'store_type', 'add_time')
    model_icon ='fa fa-folder-open-o'

class UserMessageAdmin(object):
    list_display = ('id', 'user', 'message','is_read', 'send_time')
    list_display_links = ('id', 'user', 'message')
    search_fields = ('user', 'message', 'is_read')
    list_filter = ('user', 'message', 'is_read', 'send_time')
    model_icon = 'fa fa-comments-o'


class UserCourseAdmin(object):
    list_display = ('id', 'user', 'course', 'add_time')
    list_display_links = ('user', 'course')
    search_fields = ('user', 'course', 'add_time')
    list_filter = ('user__username', 'course__name', 'add_time')
    model_icon = 'fa fa-plug'

xadmin.site.register(UserQsts, UserQstsAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserStore, UserStoreAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
