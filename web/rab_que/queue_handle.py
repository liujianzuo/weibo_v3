#!/usr/bin/env python
#_*_coding:utf-8_*_
from  Intrac.rabbit_mq_conn import Rab_conn_server
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from dao.Repository.UserinfoRepository import UserRpostry
from dao.Repository.WeiBo_Repository import WeiboRepo
import json
import time,os

from dao.Repository.TagR import Tags_handler


def create_weibo(request):

    rep = {"status":True,"message":"","data":""}
    if request.method == "GET":
        timestamp = time.time()
        print(time.time())
        user_id = request.session['userinfo']['data'][0]["user_id__id"]
        # pic_path = "statics/%s/%s" %(user_id,timestamp)
        # if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(__file__)),pic_path))
        # form_data = request.POST.get("weibo_data")
        form_data = {"text":"这是一条新的微博","perm":0,"wb_type":0,"pictures_link_id":json.dumps(['/statics/uploads/1/temp/563DE154F522BCEAF9C81A383396C066.jpg']),"user_id":user_id}
        print(form_data)
        que_name = "create_weibo_item"
        channel  = Rab_conn_server()

        channel.create_rab_queue(que_name,json.dumps(form_data))
        form_data = json.dumps(form_data)
        rep["data"] = form_data


    return HttpResponse(json.dumps(rep))


def get_new_message(request):

    if request.method == "GET":
        user_id = request.session['userinfo']['data'][0]["user_id__id"]
        channel = Rab_conn_server()

        new_weibo_count = channel.get_num_weibo("user_queue_%s" % str(user_id))

        print("get weibo item_counts",new_weibo_count)

        return HttpResponse(json.dumps({"new_weibo_count":new_weibo_count}))


def get_all_new_weibo(request):

    if request.method == "GET":
        user_id = request.session['userinfo']['data'][0]["user_id__id"]
        channel = Rab_conn_server()
        all_new_weibo = channel.get_all_new_weibo_from_que("user_queue_%s" % str(user_id))

        print("get weibo item_weibo_detail ", all_new_weibo)

        return HttpResponse(json.dumps({"all_new_weibo": all_new_weibo}))



