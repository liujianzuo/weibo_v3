#!/usr/bin/env python
#_*_coding:utf-8_*_
from dao import models



class Coment_R:

    def __init__(self):
        pass


    def create_new_weibo(self,weibo_dict):

        ret = {"status": True, "data": "", "message": ""}


        try:
            mod_obj = models.Comment.objects.create(**weibo_dict)
            view_data = {"comment_weibo": list(mod_obj),}
            print(view_data, "mode_obj")
            ret['data'] = view_data
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret
