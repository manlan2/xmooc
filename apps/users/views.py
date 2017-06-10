# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from users import models
from django.contrib.auth import authenticate, login

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from forms import LoginForm, RegisterForm

# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = models.UserProfile.objects.get(Q(username=username)|Q(email=username))
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


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})


def index(request):
    banner_list = models.Banner.objects.all()[:5]
    return render(request, 'index.html', {'banner_list':banner_list,})


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