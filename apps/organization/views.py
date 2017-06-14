# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from organization.models import CityDict, CourseOrg, Teacher
from courses.models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from forms import UserQstsForm
from django.views.generic.base import View

# Create your views here.


def teachers(request):
    
    all_teachers = Teacher.objects.all()

    search_keyword = request.GET.get('keywords', '')

    if search_keyword:
        all_teachers = Teacher.objects.filter(name__icontains=search_keyword)

    teacher_count = all_teachers.count()

    sort = request.GET.get('sort', '')

    if sort:
        all_teachers = all_teachers.order_by('-click_nums')

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_teachers, 2, request=request)

    teachers = p.page(page)

    teacher_rank = Teacher.objects.order_by('-fav_nums')
    return render(request, 'teachers-list.html', {
        'all_teachers':teachers,
        'teacher_count':teacher_count,
        'teacher_rank':teacher_rank,
        'sort':sort,})


def orgs(request):

    all_orgs = CourseOrg.objects.all()

    search_keyword = request.GET.get('keywords')

    if search_keyword:
        all_orgs = CourseOrg.objects.filter(name__icontains=search_keyword)

    org_rank = CourseOrg.objects.order_by('click_nums')[0:3]

    city_id = request.GET.get('city', '')
    category = request.GET.get('ct', '')
    sort = request.GET.get('sort', '')

    if sort:
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        else:
            all_orgs = all_orgs.order_by('-course_nums')

    if city_id:
        all_orgs = all_orgs.filter(city_id=city_id)

    if category:
        all_orgs = all_orgs.filter(category=category)

    orgs_count = all_orgs.count()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_orgs, 2, request=request)

    orgs = p.page(page)

    all_cities = CityDict.objects.all()
    return render(request, 'orgs-list.html', {
        'all_orgs':orgs,
        'all_cities':all_cities,
        'orgs_count':orgs_count,
        'city_id':city_id,
        'category':category,
        'sort':sort,
        'org_rank':org_rank,
    })


def home(request, org_id):
    org = CourseOrg.objects.get(pk=org_id)
    return render(request, 'org-home.html', {'org':org})


def org_courses(request, org_id):
    org = CourseOrg.objects.get(pk=org_id)
    return render(request, 'org-courses.html', {'org':org})


def org_teachers(request, org_id):
    org = CourseOrg.objects.get(pk=org_id)
    return render(request, 'org-teachers.html', {'org':org})


def org_desc(request, org_id):
    org = CourseOrg.objects.get(pk=org_id)
    return render(request, 'org-desc.html', {'org':org})


def detail(request, teacher_id):
    teacher_dateil = Teacher.objects.get(pk=teacher_id)
    all_courses = Course.objects.filter(teacher=teacher_dateil)
    teacher_rank = Teacher.objects.order_by('click_nums')[:3]
    return render(request, 'teacher-detail.html', {
        'teacher_dateil':teacher_dateil,
        'teacher_rank':teacher_rank,
        'all_courses':all_courses
    })


class AddQstView(View):

    def post(self, request):
        userqst_form = UserQstsForm(request.POST)
        if userqst_form.is_valid():
            user_qst = userqst_form.save(commit=True)