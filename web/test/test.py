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


def wei_bo_detail_test(request):
    if request.session.get("is_login",None):
        print(request.session['userinfo']) #{'data': [{'email': '1223995142@qq.com', 'head_img': 'statics/head_img/024B00103A7C6061429E5F1DB2913C74.png', 'follow_list__user_id': 2, 'id': 1, 'user_id__id': 1, 'age': 23, 'sex': 1, 'brief': '一江春水向东流', 'name': '刘健佐', 'tags__name': 'test'}], 'message': '', 'status': True}

        if request.method == "POST":

            pass
        else:
            username = request.session['username']
            obj_user = UserRpostry()
            user_nid = obj_user.select_nid(username)
            user_nid = user_nid['data']

            view_model = obj_user.select_follow_list_and_num(user_nid) #{'data': {'followed_num': 1, 'data': [{'age': 23, 'email': '1223995142@qq.com', 'sex': 1, 'name': '刘健佐', 'user_id__id': 1, 'follow_list__user_id': 2, 'head_img': 'statics/head_img/024B00103A7C6061429E5F1DB2913C74.png', 'brief': '一江春水向东流', 'tags__name': 'test'}], 'my_fans_num': 2}, 'message': '', 'status': True}

            wei_user = WeiboRepo()
            webo_count = wei_user.count_user_num_weibo(user_nid)
            print(webo_count)

            weibo_detail_ = wei_user.get_new_ten_weibo_item(user_nid)
            # if weibo_detail_['status']:
            weibo_detail_data = weibo_detail_['data']
            print(weibo_detail_data["weibo_detail_item"])
            # {'weibo_detail_item': [{'id': 3, 'date': datetime.datetime(2016, 9, 26, 7, 58, 57, 256159, tzinfo=<UTC>), 'text': '这是一条新的微博', 'pictures_link_id': '["/statics/uploads/1/temp/563DE154F522BCEAF9C81A383396C066.jpg"]', 'wb_type': 0, 'video_link_id': None, 'user_id': 2, 'perm': 0}, {'id': 15, 'date': datetime.datetime(2016, 9, 26, 8, 49, 15, 326685, tzinfo=<UTC>), 'text': '这是一条新的微博', 'pictures_link_id': '["/statics/uploads/1/temp/563DE154F522BCEAF9C81A383396C066.jpg"]', 'wb_type': 0, 'video_link_id': None, 'user_id': 2, 'perm': 0}, {'id': 16, 'date': datetime.datetime(2016, 9, 26, 8, 57, 20, 897298, tzinfo=<UTC>), 'text': '这是一条新的微博', 'pictures_link_id': '["/statics/uploads/1/temp/563DE154F522BCEAF9C81A383396C066.jpg"]', 'wb_type': 0, 'video_link_id': None, 'user_id': 2, 'perm': 0}, {'id': 4, 'date': datetime.datetime(2016, 9, 26, 8, 0, 3, 635208, tzinfo=<UTC>), 'text': '这是一条新的微博', 'pictures_link_id': '["/statics/uploads/1/temp/563DE154F522BCEAF9C81A383396C066.jpg"]', 'wb_type': 0, 'video_link_id': None, 'user_id': 3, 'perm': 0}, {'id': 5, 'date': datetime.datetime(2016, 9, 26, 8, 2, 4, 41588, tzinfo=<UTC>), 'text': '这是一条新的微博', 'pictures_link_id': '["/statics/uploads/1/temp/563DE154F522BCEAF9C81A383396C066.jpg"]', 'wb_type': 0, 'video_link_id': None, 'user_id': 3, 'perm': 0}]}
            for i in weibo_detail_data["weibo_detail_item"]:
            #     print(type(i))
                index_num = weibo_detail_data["weibo_detail_item"].index(i)
                weibo_detail_data["weibo_detail_item"][index_num]["pictures_link_id"] = json.loads(weibo_detail_data["weibo_detail_item"][index_num]["pictures_link_id"])
            print(weibo_detail_data)
            infomation  = {}
            if view_model["status"]:
                infomation["followed_num"] = view_model['data']['followed_num']
                infomation['my_fans_num'] = view_model['data']['my_fans_num']
                infomation['userinfo'] = request.session['userinfo']['data'][0]
                infomation["webo_count"] = webo_count['data']['count_user_weibo']
                infomation["username"] = username
                infomation["weibo_detail_data"] = weibo_detail_data


            # ret = json.dumps(infomation)

        return render(request,"test/index1.html",{'is_login':True,'infomation':infomation})

    return render(request, "test/index1.html", {'is_login': False,})