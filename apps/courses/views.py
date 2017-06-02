from django.shortcuts import render
from django.http import HttpResponse
from courses import models

# Create your views here.


def courses(request):
    # sort = request.GET['sort']
    # if sort == ''
    course_list = models.Course.objects.all()
    course_hot = models.Course.objects.order_by('fav_nums')
    return render(request, 'courses-list.html', {'course_list':course_list,'coure_hot':course_hot})
