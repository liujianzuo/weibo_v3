#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

def index(request):
    if request.session.get("is_login",None):
        print("首页测试")
        return render(request,"index/index.html",{'is_login':True,})
    return render(request, "index/index.html", {'is_login': False,})


def lay_out(request):

    print("首页测试")
    return render(request,"lay_out/lay_out.html")

def test_lay_out(request):

    print("首页测试")
    return render(request,"_lay_mu_out/_layout.html")


