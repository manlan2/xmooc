# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from users.models import UserProfile, EmailVerifyRecord, Banner
from operation.models import UserCourse
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
                return render(request, 'login.html', {'msg': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误！'})


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

            return render(request, 'register.html', {'register_form':register_form, 'msg':'输入有误！'})


def index(request):
    banner_list = Banner.objects.all()[:5]
    return render(request, 'index.html', {'banner_list':banner_list,})


def usercenter_info(request, user_id):
    user = UserProfile.objects.get(pk=user_id)
    return render(request, 'usercenter-info.html', {'user':user})


def usercenter_mycourse(request, user_id):
    user_course = UserCourse.objects.filter(user_id=user_id)
    users_id = user_id
    return render(request, 'usercenter-mycourse.html', {'user_course':user_course,'id':users_id})


def usercenter_mystore(request, user_id):
    return render(request, 'usercenter-mystore.html')


def usercenter_mymessage(request, user_id):
    return render(request, 'usercenter-mymessage.html')