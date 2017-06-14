# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from users.models import UserProfile, EmailVerifyRecord, Banner
from operation.models import UserCourse, UserStore, UserMessage
from courses.models import Course
from django.contrib.auth import authenticate, login

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from forms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password

# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return  None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})
    def post(self, request):

        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': u'用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'login_form':login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.save()
            return render(request, 'login.html')
        else:

            return render(request, 'register.html', {'register_form':register_form, 'msg':u'输入有误！'})


def index(request):
    banner_list = Banner.objects.all()[:5]
    course_big = Course.objects.order_by('click_nums')[:2]
    course_small = Course.objects.order_by('click_nums')[2:6]
    return render(request, 'index.html', {
        'banner_list':banner_list,
        'course_big':course_big,
        'course_small':course_small,
    })


def usercenter_info(request, user_id):
    user = UserProfile.objects.get(pk=user_id)
    return render(request, 'usercenter-info.html', {'user':user})


def usercenter_mycourse(request, user_id):
    user_course = UserCourse.objects.filter(user_id=user_id)
    users_id = user_id
    return render(request, 'usercenter-mycourse.html', {
        'user_course':user_course,
        'id':users_id
    })


def usercenter_mystore(request, user_id):
    courses_store = UserStore.objects.filter(user_id=user_id).filter(store_type=1)
    orgs_store = UserStore.objects.filter(user_id=user_id).filter(store_type=2)
    teachers_store = UserStore.objects.filter(user_id=user_id).filter(store_type=3)
    return render(request, 'usercenter-mystore.html', {'user_id':user_id})


def usercenter_mymessage(request, user_id):
    messages = UserMessage.objects.filter(user=user_id)
    return render(request, 'usercenter-mymessage.html', {'user_id':user_id})
	
	
def userinfo_save(request, user_id):
    nick_name = request.POST.get('nick_name', '')
    birthday = request.POST.get('birthday', '')
    gender = request.POST.get('gender', '')
    address = request.POST.get('address', '')
    mobile = request.POST.get('mobile', '')
	
	
	