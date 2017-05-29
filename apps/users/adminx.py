# -*- coding:utf-8 -*-

import xadmin
from .models import EmailVerifyRecord, Banner

class EmailVerifyRecordAdmin(object):
    #展示字段
    list_display = ('id','code','email','type','send_time')
    #超链接字段
    list_display_links = ('id','code')
    #搜索字段
    search_fields = ('code','email','type')
    #过滤字段
    list_filter = ('code','email','type','send_time')


class BannerAdmin(object):
    list_display = ('id', 'title', 'image', 'url', 'index','add_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'index')
    list_filter = ('title', 'url', 'index', 'add_time')


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)