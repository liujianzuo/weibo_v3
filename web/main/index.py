#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from dao.Repository.UserinfoRepository import UserRpostry
from dao.Repository.WeiBo_Repository import WeiboRepo
import json

def index(request):
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


            infomation  = {}
            if view_model["status"]:
                infomation["followed_num"] = view_model['data']['followed_num']
                infomation['my_fans_num'] = view_model['data']['my_fans_num']
                infomation['userinfo'] = request.session['userinfo']['data'][0]
                infomation["webo_count"] = webo_count['data']['count_user_weibo']
                infomation["username"] = username


            # ret = json.dumps(infomation)


        return render(request,"index/index.html",{'is_login':True,'infomation':infomation})






    return render(request, "index/index.html", {'is_login': False,})


def lay_out(request):
    if not request.session.get("is_login", None):
        return redirect("/login")
    return render(request,"lay_out/lay_out.html",{'is_login': False,})

def test_lay_out(request):
    if request.session.get("is_login", None):
        print("首页测试")
        return render(request, "index/index.html", {'is_login': True,})
    return render(request,"_lay_mu_out/_layout.html",{'is_login': False,})


