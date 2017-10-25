# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from courses.models import Course, Lesson, Video, CourseResource
from operation.models import UserCourse,CourseComments
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic.base import View

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

    tag = course.tag
    if tag:
        relate_courses = Course.objects.filter(tag=tag)[1:2]
    else:
        relate_courses = []
    all_lessons = Lesson.objects.filter(course_id=course_id)
    lesson_nums = all_lessons.count()
    return render(request, 'course-detail.html', {
        'course':course,
        'lesson_nums':lesson_nums,
        'relate_courses':relate_courses,
    })


def lesson(request, course_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:login'))

    user_course = UserCourse()

    #我的课程添加
    course_ids = ''

    for all_courses_ids in UserCourse.objects.filter(user_id=request.user.id):
        course_ids += str(all_courses_ids.course_id)

    if course_id not in course_ids:
        user_course.user_id = int(request.user.id)
        user_course.course_id = int(course_id)
        user_course.save()

    course = Course.objects.get(pk=int(course_id))

    course.students += 1
    course.save()

    all_lessons = Lesson.objects.filter(course_id=course_id)
    all_resources = CourseResource.objects.filter(course_id=course_id)
    return render(request, 'course-video.html', {
        'course': course,
        'all_lessons': all_lessons,
        'all_resources': all_resources,
    })


def comment(request, course_id):
    course = Course.objects.get(pk=int(course_id))
    all_resources = CourseResource.objects.filter(course_id=course_id)
    all_comments = CourseComments.objects.all()

    return render(request, 'course-comment.html', {
        'course': course,
        'all_resources':all_resources,
        'all_comments':all_comments,
    })


class VideoPlayView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course

        all_lessons = Lesson.objects.filter(course_id=course.id)
        all_resources = CourseResource.objects.filter(course_id=course.id)
        return render(request, 'course-play.html', {
            'course': course,
            'all_lessons': all_lessons,
            'all_resources': all_resources,
            'video': video,
        })


class CommentView(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=int(course_id))
        all_resources = CourseResource.objects.filter(course_id=course_id)
        all_comments = CourseComments.objects.all()

        return render(request, 'course-comment.html', {
            'course': course,
            'all_resources': all_resources,
            'all_comments': all_comments,
        })


class AddCommentsView(View):
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get('course_id', 0)
        comments = request.POST.get('comments', '')
        if course_id > 0 and comments:
            course_comment = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comment.course = course
            course_comment.comments = comments
            course_comment.user = request.user
            course_comment.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


