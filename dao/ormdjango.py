#!/usr/bin/env python
#_*_coding:utf-8_*_

from dao import models
from django.contrib.auth.hashers import make_password, check_password


def get_user_info(user,pwd):
    req = {'status':True,'message':""}
    # ret = models.UserInfo.objects.all() # <QuerySet []> 内部是{表字段}
    try:
        ret = models.UserInfo.objects.filter(name=user) # <QuerySet []> 内部是{表字段}
        if len(ret) >0:
            req['status'] = False
            req['message'] = "用户已存在"
        else:
            models.UserInfo.objects.create(name=user,password=pwd)
    except Exception as e:
        req['status'] = False
        ret["message"] = e

    return req

def login_user(user,pwd,md5pwd):
    req = {'status': True, 'message': ""}
    # ret = models.UserInfo.objects.all() # <QuerySet []> 内部是{表字段}
    try:
        ret = models.UserInfo.objects.filter(name=user)  # <QuerySet []> 内部是{表字段}
        if len(ret) == 0:
            req['status'] = False
            req['message'] = "用户不存在"
        else:
            nx = check_password(pwd,md5pwd)
            if not nx:
                req['status'] = False
                req['message'] = "用户名或者密码不正确"
    except Exception as e:
        req['status'] = False
        req["message"] = e

    return req


def publish(*args):
    req = {'status': True, 'message': ""}
    u = args[4]
    try:
        user_id = models.UserInfo.objects.filter(name=u).values("id")
        print(user_id[0]['id'])
        user_id = user_id[0]['id']
        models.News.objects.create(
            title=args[0],
            summary=args[1],
            content=args[2],
            img=args[3],
            user_news_id_id=user_id,
        )
    except Exception as e:
        req['status'] = False
        req["message"] = e

    return req


def get_all_article():

    ret = models.News.objects.all().values("id","title","summary","img","create_date","user_news_id__name")
    return ret