# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True,error_messages={'invalid':u'用户名不能为空'})
    password = forms.CharField(required=True, min_length=6, error_messages={'invalid':u'密码不能为空并大于6个字符'})


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={'invalid':u'验证码有误！'})
