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

from dao import models
from django.core.paginator import  Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from decimal import Decimal
from service.home import pages

from service.manage import article as art
from service.manage import pubartichle as pablish
'''
# >>> make_password(123, "salt", 'pbkdf2_sha256')
# 'pbkdf2_sha256$30000$salt$HqrtiEeP29fCF8lIOaHblAb+X4kOQdWqXgq1MIv8CGE='
# >>> a = make_password(123, "salt", 'pbkdf2_sha256')
# >>> b=123
# >>> check_password(b,a)
# True
'''



def blog(request):
    username = request.session.get("username",None)
    ret = pages.Pager(request)
    # {'username': username},
    p = ret[0]
    page_range = ret[1]
    book_list = ret[2]

    username = username
    return render(request,"index_views/blog.html",locals())

def pub(request):
    s = request.session.get("is_login",None)
    u = request.session.get("username",None)
    if s and u:
        print(s,u)
        if request.method == 'POST':
            ret = pablish.fabu(request,u)
            if ret['status']:
                return redirect("/blog/")
            else:
                a = mark_safe("<a href='/pub/'>%s</a>" % ret["message"])
                return HttpResponse(a)

        return render(request,"manage/publish.html",{'username':u})

    return redirect("/login")


def article(request):
    username = request.session.get("username",None)
    s = request.session.get("is_login", None)
    # if s and username:
    print(request.GET.get("news_id",None))
    news_id = request.GET.get("news_id",None)
    ret = art.get_article(request,news_id)
    ret = list(ret)
    print(ret,23423432523512312)
    return render(request,"article_final/article.html",{"username":username,"article":ret})
    # return redirect("/login")
