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
            models.Comment.objects.create(**weibo_dict)
            # mod_obj = models.Comment.objects.create(**weibo_dict)
            # view_data = {"comment_weibo": list(mod_obj),}
            print(1111,weibo_dict)

            # print(view_data, "mode_obj")
            ret['data'] = "添加成功"
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret


    def get_all_cur_weibo_id_coment(self,weibo_id):
        ret = {"status": True, "data": "", "message": ""}
        print("shujuceng",weibo_id)
        try:
            mod_obj = models.Comment.objects.filter(to_weibo=weibo_id).values("id","comment","comment_type", "to_weibo","p_comment","date","user__name").order_by("-id")
            # mod_obj = models.Comment.objects.create(**weibo_dict)
            view_data = {"comment_weibo": list(mod_obj),}
            print(1111, view_data)

            # print(view_data, "mode_obj")
            ret['data'] = view_data
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret