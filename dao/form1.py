#!/usr/bin/env python
#_*_coding:utf-8_*_
from django import forms
from dao import models


class Form1(forms.Form):
    username = forms.CharField(
        max_length=32,
        error_messages={'required':"用户名不能为空","invalid":"用户名格式错误"}
    )  # 前端name值input的
    password = forms.CharField(
        max_length=32,
        min_length=3,
        error_messages={'required':"密码不能为空","invalid":"密码格式错误"}
    )
