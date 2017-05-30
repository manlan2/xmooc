# -*- coding:utf-8 -*-

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views

#后台全局配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'XMOOC'
    site_footer = '北京牛逼公司'
    menu_style = 'accordion'


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

#注册models
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

#注册BaseSetting
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)