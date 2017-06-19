# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from operation.models import CourseComments, UserStore
from courses.models import Course, CourseResource
import json

# Create your views here.


def comment(request, course_id):
    course = Course.objects.get(pk=course_id)
    all_comments = CourseComments.objects.filter(course_id=course_id)
    all_resources = CourseResource.objects.filter(course_id=course_id)
    return render(request, 'course-comment.html', {
        'course': course,
        'all_comments': all_comments,
        'all_resources':all_resources
    })


def addstore(request):
    store_id = request.POST.get('fav_id', '')
    store_type = request.POST.get('fav_type', '')
	
    json_data = {'msg':u'用户未登录','status':'fail'}
	
	
    if not request.user.is_authenticated():
        return HttpResponse(json.dumps(json_data),content_type="application/json")
    
	exist_record = UserStore.objects.filter(user=request.user, store_id=store_id, store_type=store_type)
	
	if exist_record:
		exist_record.delete()
		json_data = {'msg':u'收藏','status':'success'}
		return HttpResponse(json.dumps(json_data),content_type="application/json")
	else:
	
		user_store = UserStore()
		user_store.user_id = request.user.id
		user_store.store_id = int(store_id)
		user_store.store_type = int(store_type)
		user_store.save()
		
		has_stored = True
		json_data = {'msg':u'已收藏','status':'success'}
		return HttpResponse(json.dumps(json_data),content_type="application/json")