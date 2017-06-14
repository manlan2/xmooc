# -*- coding:utf-8 -*-
from django import forms
from operation.models import UserQsts


class UserQstsForm(forms.ModelForm):

    class Meta:
        model = UserQsts
        fields = ['name', 'mobile', 'course_name']