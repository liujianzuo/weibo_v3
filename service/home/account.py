#!/usr/bin/env python
#_*_coding:utf-8_*_

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password

'''
>>> from django.contrib.auth.hashers import make_password, check_password

# >>> make_password(123, "salt", 'pbkdf2_sha256')
# 'pbkdf2_sha256$30000$salt$HqrtiEeP29fCF8lIOaHblAb+X4kOQdWqXgq1MIv8CGE='
# >>> a = make_password(123, "salt", 'pbkdf2_sha256')
# >>> b=123
# >>> check_password(b,a)
True
'''

from dao.form1 import Form1
from dao.ormdjango import *

def login(request):
    # 验证
    flag = {}
    f = Form1(request.POST)  # 将所有数据验证
    if f.is_valid():
        print(f.cleaned_data)  # 提交争取数据f.cleaned_data
        flag["status"] = True
        flag["error"] = ""
        pwd = request.POST.get('password')
        password = make_password(pwd, "salt", 'pbkdf2_sha256')
        r = login_user(request.POST.get('username'),pwd, password, )
        print(r, 123131414141)
        if not r['status']:
            flag['status'] = False
            flag['error'] = {'username': [r['message']]}  # 模拟django的form表单错误格式
        else:
            request.session['is_login'] = True
            request.session['username'] = request.POST.get('username')
    else:
        print(type(f.errors), f.errors)
        flag["status"] = False
        flag["error"] = f.errors

    return flag


def register(request):
    # 验证
    flag = {}
    f = Form1(request.POST) #将所有数据验证
    if f.is_valid():
        print(f.cleaned_data) #  提交争取数据f.cleaned_data
        flag["status"] = True
        flag["error"] = ""
        pwd = request.POST.get('password')
        password = make_password(pwd, "salt", 'pbkdf2_sha256')
        r = get_user_info(request.POST.get('username'),password,)
        if not r['status']:
            flag['status']=False
            flag['error']= {'username':[r['message']]} # 模拟django的form表单错误格式
    else:
        print(type(f.errors),f.errors)
        flag["status"] = False
        flag["error"] = f.errors

    return flag


