#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
from dao import models
from dao import ormdjango as orm

def fabu(request,u):
    ret = {"status":True,"message":""}
    title = request.POST.get("title", None)
    summary = request.POST.get("summary", None)
    content = request.POST.get("content", None)
    file = request.FILES.get("file", None)
    print(all([title, summary, content, file]))
    if all([title, summary, content, file]):

        PATH = os.path.join("web/statics/img/upload/", file.name)
        f = open(PATH, "wb")
        for chunk in file.chunks():
            f.write(chunk)
        print(title, summary, content, file,u)
        file = "/statics/img/upload/%s" % file.name
        x = orm.publish(title,summary,content,file,u)
        print(x)
        if not x["status"]:
            ret['status'] = False
            ret['message'] = "发布文章到数据库时候服务器出错,联系管理员%s" % x['message']
    else:
        ret['status'] =False
        ret['message'] = "有内容为空请返回重新提交"

    return ret