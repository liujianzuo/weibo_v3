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

    def get_new_ten_weibo_item(self,user_nid):
        ret = {"status": True, "data": "", "message": ""}
        try:
            if user_nid:
                nid = int(user_nid)
                nid_list_followed = []
                ret1 = models.UserProfile.objects.filter(user_id__id=nid).values("follow_list__user_id", )  # <QuerySet [{'follow_list__user_id': 1}]>
                for item in ret1:
                    nid_list_followed.append(item['follow_list__user_id'])
                nid_list_followed.append(nid)
                print(nid_list_followed)

                model_obj = models.Weibo.objects.filter(user_id__in=nid_list_followed).values("wb_type", "id", "text",
                                                                                        "pictures_link_id",
                                                                                        "video_link_id", "perm", "date",
                                                                                        "user_id","user__user__username","user__name")



            view_data = {"weibo_detail_item": list(model_obj),}
            print(view_data, "view_model")
            ret['data'] = view_data
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret