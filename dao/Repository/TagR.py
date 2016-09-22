#!/usr/bin/env python
#-*-coding:utf-8-*-

from dao import models

class Tags_handler:
    def __init__(self):
        pass


    def insert_tags(self,name):
        ret = {'status':None,'messages':'','error':''}
        try:
            model = models.Tags.objects.create(name=name)
            print(type(model))
            ret['status']=True
        except Exception as e:
            ret['messages']=e
        return  ret


    def exist_tags(self,name):
        ret = {'status': None, 'messages': '', 'error': ''}
        model=models.Tags.objects.filter('name').first()
        try:
            if model:
                ret['status'] = True
            else:
                models.Tags.objects.create(name=name)
        except Exception as e:
            ret['messages'] = e
        return ret

    def fetch_tags_id(self,name):
        tag_id=[]
        # models.UserProfile.objects.filter(name='').

    def insert_dao_userprofile_tags(self):
        pass



