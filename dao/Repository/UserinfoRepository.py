#-*-coding:utf-8-*-
from django.db import models
from dao.migrations.models import *
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

def AddTags(request):

    tags_obj = models.UserProfile.objects.filter(tags='').first()
    print(tags_obj)
    models.UserProfile.objects.create(caption='')
    aa = models.UserProfile.objects.filter(caption='').all().values('book__name', 'book__page', 'caption')
    print(aa)

    models.Tb1.objects.filter(name='seven').update(gender='0')
    return HttpResponse('添加成功')