#!/usr/bin/env python
#_*_coding:utf-8_*_
import time
import os
import hashlib
import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required


from weibo import settings
from dao import models

from Intrac import redis_conn

# redis_cccon= redis_conn.conn_redis(settings)

def login(request):
    ret = {"status":True,"message":""}
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        import os
        if user:
            django_login(request,user)
            path_dir = settings.FILE_CENTER_PATH
            user_dir = "%s/%s" % (path_dir,request.user.userprofile.id)
            if not os.path.exists(user_dir):
                os.makedirs(user_dir)
                os.makedirs(user_dir + "/temp")

            #
            request.session['is_login'] = True



            #设置活跃用户
            # redis_cccon.set("active_%s" % user.userprofile.id, True, ex=3600*12) #半天
            ret["message"] = "登录成功"

        else:
            ret["status"] = False
            ret["message"] = "登录失败"

    return HttpResponse(json.dumps(ret))


def logout(request):

    request.session['is_login'] = False

    return redirect("/index")
