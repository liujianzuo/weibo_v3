#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

from dao import models

class UserRpostry:

    def AddTags(self):

        tags_obj = models.UserProfile.objects.filter(tags='').first()
        print(tags_obj)
        models.UserProfile.objects.create(caption='')
        aa = models.UserProfile.objects.filter(caption='').all().values('book__name', 'book__page', 'caption')
        print(aa)

        models.Tb1.objects.filter(name='seven').update(gender='0')
        return HttpResponse('添加成功')



    def select_follow_list_and_num(self,nid):
        ret = {"status":True,"data":"","message":""}

        try:

            if nid:
                nid = int(nid)
                data = list(models.UserProfile.objects.filter(user_id__id=nid).values("id","email", "name", "brief", "sex", "age",
                                                                                "user_id__id", "head_img",
                                                                                "follow_list__user_id"))
                fans_data = list(models.UserProfile.objects.filter(user_id__id=nid).values("my_followers__user_id"))

            view_model = {"followed_num":len(data),"data":data,"my_fans_num":len(fans_data)}
            ret['data']= view_model
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret


    def select_nid(self,name):
        ret = {"status": True, "data": "", "message": ""}
        try:

            nid_list = list(models.UserProfile.objects.filter(user__username=name).values("user_id"))

            if nid_list:
                nid = int(nid_list[0]['user_id'])
                ret['data'] = nid
            else:
                ret['message'] = "用户不存在,系统有漏洞被无效用户登录"
                ret["status"] = False
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret


    def select_all_one_user_msg(self, name):
        ret = {"status": True, "data": "", "message": ""}
        try:

            nid_list = list(models.UserProfile.objects.filter(user__username=name).values("user_id"))
            if nid_list:
                nid = int(nid_list[0]['user_id'])
                print(nid)
                view_data  = models.UserProfile.objects.filter(user_id__id=nid).values('id',"email", "name", "brief", "sex", "age",
                                                                                "user_id__id", "head_img",
                                                                                "follow_list__user_id")
                ret["data"] = list(view_data)
            else:
                ret['message'] = "用户不存在,系统有漏洞被无效用户登录"
                ret["status"] = False
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret


    #正向从profile插入tag

    def insert_tag_from_profile(self,nid,tag_list):
        ret = {"status": True, "data": "", "message": ""}
        try:
            print(tag_list,1111111123123)
            new_list = []
            obj = models.UserProfile.objects.get(id=nid)
            for item in tag_list:
                new_list.append(models.Tags.objects.get(name=item))

            data_model = obj.tags.add(*new_list)
            ret['data'] = data_model
        except Exception as e:

            ret['message'] = e
            ret["status"] = False

        return ret




