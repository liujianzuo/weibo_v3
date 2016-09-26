#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from dao.Repository.UserinfoRepository import UserRpostry
from dao.Repository.WeiBo_Repository import WeiboRepo
import json

from dao.Repository.TagR import Tags_handler

import os

def file_up(request):
    print(request)
    print(request.FILES.get("fff"))
    if request.method == "POST":

        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"statics/uploads/1/temp",)
        obj = request.FILES.get("fff")
        print(obj.name, obj.chunks(), type(obj.chunks()))

        f = open(os.path.join(path,obj.name), "wb")
        for chunk in obj.chunks():
            f.write(chunk)
    return render(request,"test/test.html")
