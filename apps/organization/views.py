from django.shortcuts import render
from django.http import HttpResponse
from organization import models
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def teachers(request):
    teacher_list = models.Teacher.objects.all()
    teacher_rank = models.Teacher.objects.order_by('fav_nums')
    return render(request, 'teachers-list.html', {'teacher_lsit':teacher_list,'teacher_rank':teacher_rank})


def orgs(request):
    all_orgs = models.CourseOrg.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    # Provide Paginator with the request object for complete querystring generation

    p = Paginator(all_orgs, 1, request=request)

    orgs = p.page(page)

    all_cities = models.CityDict.objects.all()
    return render(request, 'orgs-list.html', {'all_orgs':orgs,'all_cities':all_cities})


