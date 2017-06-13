# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson, Video, CourseResource
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.


def courses(request):

    all_courses = Course.objects.all()

    search_keyword = request.GET.get('keywords', '')

    if search_keyword:
        all_courses = Course.objects.filter(name__icontains=search_keyword)

    sort = request.GET.get('sort', '')

    if sort:
        if sort == 'hot':
            all_courses = all_courses.order_by('-click_nums')
        else:
            all_courses = all_courses.order_by('-students')

    orgs_count = all_courses.count()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_courses, 6, request=request)

    courses = p.page(page)

    course_hot = Course.objects.order_by('fav_nums')[:3]
    return render(request, 'courses-list.html', {
        'all_courses':courses,
        'sort':sort,
        'coure_hot':course_hot,
    })



def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)

    course.click_nums += 1
    course.save()

    all_lessons = Lesson.objects.filter(course_id=course_id)
    lesson_nums = all_lessons.count()
    return render(request, 'course-detail.html', {'course':course,'lesson_nums':lesson_nums})


def lesson(request, course_id):
    course = Course.objects.get(pk=course_id)
    all_lessons = Lesson.objects.filter(course_id=course_id)
    all_resources = CourseResource.objects.filter(course_id=course_id)
    return render(request, 'course-video.html', {
        'course': course,
        'all_lessons': all_lessons,
        'all_resources': all_resources,
    })


