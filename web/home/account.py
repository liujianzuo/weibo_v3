#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
# >>> make_password(123, "salt", 'pbkdf2_sha256')
# 'pbkdf2_sha256$30000$salt$HqrtiEeP29fCF8lIOaHblAb+X4kOQdWqXgq1MIv8CGE='
# >>> a = make_password(123, "salt", 'pbkdf2_sha256')
# >>> b=123
# >>> check_password(b,a)
True
'''

import time
import os
import hashlib
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from dao import models

from service.home import account as sign

def login(request):

    if request.session.get("is_login",None):
        username = request.session['username']
    else:
        username = None
    if request.method == "POST":
        ret = sign.login(request)
        if ret["status"]:
            print(username)
            return redirect("/blog/")
        else:
            return render(request,"home/register.html",{"error":ret["error"],})
    return render(request,"home/register.html",{"error":None,"username":username})
    # return HttpResponse("login")


def register(request):
    print(request.method)
    if request.method == "POST":
        ret = sign.register(request)
        if ret["status"]:

            return redirect("/login/")
        else:
            return render(request,"home/login.html",{"error":ret["error"]})
    return render(request,"home/login.html",{"error":None})


def logout(request):

    request.session['is_login'] = False
    request.session['username'] = None
    return redirect("/blog/")