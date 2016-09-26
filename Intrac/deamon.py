#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weibo.settings")

import django
django.setup()


import json

from weibo import settings
from dao import models

from Intrac import redis_conn as Rdies_conn
from  Intrac.rabbit_mq_conn import Rab_conn_server
from web.rab_que import queue_handle



class WbHandler:

    def __init__(self):
        self.redis_conn = Rdies_conn.conn_redis(settings)
        self.rab_obj = Rab_conn_server()
        self.channel = self.rab_obj.channel


    def save_weibo_to_db(self,data):

        # if not data["pic_img"]:
        weibo_obj = models.Weibo.objects.create(**data)
        # else:
        #     pass


        return weibo_obj


    # 将新微博数据对象根据redis的关注的活跃用户 进行推送
    def push_to_followers(self,data,weibo_obj):
        '''
        只推送最近一天登录的关注者
        :param data:
        :return:
        '''
        print("---把新wb推给所有关注者")
        data['wb_id'] = weibo_obj.id
        # wb_user = models.UserProfile.objects.get(id=data.get("user_id"))
        wb_user = models.UserProfile.objects.get(id=data.get("user_id"))
        print(wb_user.my_followers.select_related())

        for follower in wb_user.my_followers.select_related():
            queue_name = "user_queue_%s" % follower.id
            print("q_name",queue_name)
            #检测用户是否最近登录了,登录 了就给他推送

            login_recently_flag = self.redis_conn.get("active_%s" %follower.id)
            print("最近是否登录,",follower.id,login_recently_flag)
            # login_recently_flag = str(login_recently_flag,encoding='utf-8')

            print(123124124,login_recently_flag,type(login_recently_flag))
            print(type(data),data)

            if login_recently_flag:

                #self.q_man.channel.queue_declare(queue=queue_name,passive=True)
                self.rab_obj.create_rab_queue(queue_name,json.dumps(data))
                # self.channel.queue_declare(queue=queue_name)
                #
                # self.channel.channel.basic_publish(exchange='',
                #                       routing_key=queue_name,
                #                       body=json.dumps(data))
                print(" [x] Sent to %s " % queue_name,data)


    def callback(self,ch, method, properties, body):
        print(" [x] Received %r" % body)
        data = json.loads(body.decode())
        db_wb_obj = self.save_weibo_to_db(data)
        print(data,db_wb_obj.id)
        self.push_to_followers(data,db_wb_obj)

    def watch_new_wbs(self):
        '''监听所有新发的微博'''

        queue_name ='create_weibo_item'


        self.channel.basic_consume(self.callback,
                              queue=queue_name,
                              no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()




