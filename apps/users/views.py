from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def userlogin(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})

def courses(request):
    return render(request, 'courses-list.html', {})


def teachers(request):
    return render(request, 'teachers-list.html', {})


def orgs(request):
    return render(request, 'orgs-list.html', {})


def usercenter_info(request):
    return render(request, 'usercenter-info.html')


def usercenter_mycourse(request):
    return render(request, 'usercenter-mycourse.html')


def usercenter_mystore(request):
    return render(request, 'usercenter-mystore.html')


def usercenter_mymessage(request):
    return render(request, 'usercenter-mymessage.html')