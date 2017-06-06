from django.shortcuts import render
from django.shortcuts import HttpResponse
from users import models

# Create your views here.


def index(request):
	banner_list = models.Banner.objects.all()[:5]
	return render(request, 'index.html', {
					'banner_list':banner_list,
					})


def userlogin(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})


def usercenter_info(request):
    return render(request, 'usercenter-info.html')


def usercenter_mycourse(request):
    return render(request, 'usercenter-mycourse.html')


def usercenter_mystore(request):
    return render(request, 'usercenter-mystore.html')


def usercenter_mymessage(request):
    return render(request, 'usercenter-mymessage.html')