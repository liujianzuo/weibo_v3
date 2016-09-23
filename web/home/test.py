#!/usr/bin/env python
#-*-coding:utf-8-*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from dao import models
from dao.Repository import TagR

def test(request):

    # obj=TagR.Tags_handler()
    # obj.insert_tags(name='test')
    #
    from dao.Repository.UserinfoRepository import UserRpostry
    nid = request.GET.get("nid",1)
    # # ret2 = list(models.UserProfile.objects.filter(user__username="liu").values("user_id"))[0]['user_id']
    # obj = UserRpostry()
    # ret2 = obj.select_all_one_user_msg("liu")
    # ret = models.UserProfile.objects.filter(user_id__id=nid).values('id',"email","name","brief","sex","age","user_id__id","head_img","tags__name","follow_list__user_id",)
    # ret = models.UserProfile.objects.filter(user_id__id=nid).values('name',"tags__name",)
    # ret1 = models.UserProfile.objects.filter(user_id__id=nid).values("my_followers__user_id")
    # print(11111,len(ret1),ret1,2222,ret2)


    test1="name"
    coloume_val = "玄霸天下"
    dict = {test1:coloume_val}
    ret = models.UserProfile.objects.filter(id=nid).update(**dict)

    # ret = models.Weibo.objects.filter(user_id=1)
    if not ret:
        print(123123)
    print(ret)

    return HttpResponse(ret)