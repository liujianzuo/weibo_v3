#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

from dao import models

class WeiboRepo:

    def __init__(self):
        pass


    def count_user_num_weibo(self,user_nid):
        ret = {"status": True, "data": "", "message": ""}
        try:
            if user_nid:
                nid = int(user_nid)
                data = models.Weibo.objects.filter(user_id=nid)
                if not data:
                    data = 0
                else:
                    data = len(data)

            view_model = {"count_user_weibo": data, }
            print(view_model,"view_model")
            ret['data'] = view_model
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret