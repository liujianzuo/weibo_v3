#!/usr/bin/env python
#_*_coding:utf-8_*_
from dao import models



class Coment_R:

    def __init__(self):
        pass


    def create_new_weibo(self,weibo_dict):

        ret = {"status": True, "data": "", "message": ""}


        try:
            print(weibo_dict)
            models.Comment.objects.create(**{'comment_type': 0, 'to_weibo_id': 45, 'comment': 'sdafasdgsdg', 'user_id': 1})
            # mod_obj = models.Comment.objects.create(**weibo_dict)
            # view_data = {"comment_weibo": list(mod_obj),}
            print(1111,weibo_dict)

            # print(view_data, "mode_obj")
            # ret['data'] = view_data
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret
