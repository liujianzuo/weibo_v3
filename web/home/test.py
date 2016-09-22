#!/usr/bin/env python
#-*-coding:utf-8-*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from dao import models
from dao.Repository import TagR

def test(request):

    obj=TagR.Tags_handler()
    obj.insert_tags(name='test')





    return HttpResponse('ok')