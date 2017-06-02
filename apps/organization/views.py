from django.shortcuts import render
from django.http import HttpResponse
from organization import models

# Create your views here.

def teachers(request):
    teacher_list = models.Teacher.objects.all()
    teacher_rank = models.Teacher.objects.order_by('fav_nums')
    return render(request, 'teachers-list.html', {'teacher_lsit':teacher_list,'teacher_rank':teacher_rank})


def orgs(request):
    org_list = models.CourseOrg.objects.all()
    city_list = models.CityDict.objects.all()
    return render(request, 'orgs-list.html', {'org_list':org_list,'city_list':city_list})


