#!/usr/bin/env python
#_*_coding:utf-8_*_

from dao import models

def get_article(request,id):

    ret = models.News.objects.filter(id=id).values("id","title","content","create_date","user_news_id__name")
    # print(ret)
    return ret