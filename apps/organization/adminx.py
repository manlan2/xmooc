# -*- coding:utf-8 -*-

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ('id', 'name', 'desc', 'add_time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'desc')
    list_filter = ('name', 'desc', 'add_time')
    list_export = ('xls', 'xml', 'json')
    list_editable = ['add_time', 'name']
    #model_icon = 'fa fa-building'


class CourseOrgAdmin(object):
    list_display = ('id', 'name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time')
    list_display_links = ('id', 'name', 'desc')
    search_fields = ('name', 'city')
    list_filter = ('name', 'click_nums', 'city', 'add_time')
    #model_icon = 'fa fa-university'


class TeacherAdmin(object):
    list_display = ('id', 'org', 'name', 'work_years', 'work_company', 'add_time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'org', 'work_years')
    list_filter = ('name', 'org__name', 'add_time')
    model_icon = 'fa fa-users'

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
