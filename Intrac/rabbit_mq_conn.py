#!/usr/bin/env python
#_*_coding:utf-8_*_

import pika
from weibo import settings

import json
class Rab_conn_server:

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.rabbit_host))   #链接rabbitmq
        self.channel = self.connection.channel()


    def create_rab_queue(self,name,body):
        self.channel.queue_declare(queue=name)

        self.channel.basic_publish(exchange='',routing_key=name,body=body)  # 这里的exchange为空时exchange不工作，单独的客户端服务端就只用一个队列来通信  注意body主体信息
        print(" [x] Sent 'Hello World!'")
        # self.connection.close()


    def get_num_weibo(self,user_id_que_name):
        '''返回此用户队列里新微博条数'''
        self.response = None
        self.new_wb_list = []
        detail_status = self.channel.queue_declare(queue=user_id_que_name)
        print("[%s] message count " % user_id_que_name, detail_status.method.message_count)

        return detail_status.method.message_count

    def on_response_callback(self, ch, method, props, body):
        print("new wb is comming ...", ch, method, props, body)
        self.new_wb_list.append(json.loads(body.decode()))
        self.response = True


    def get_all_new_weibo_from_que(self,user_id_que_name):
        '''
                返回此用户的新wb列表
                :param queue_name:
                :return:
                '''
        self.response = None
        self.new_wb_list = []
        status = self.channel.queue_declare(queue=user_id_que_name)
        print("[%s] message count " % user_id_que_name, status.method.message_count)

        consume_obj = self.channel.basic_consume(self.on_response_callback, no_ack=True,
                                                 queue=user_id_que_name)

        self.connection.process_data_events()
        print(" self.connection.process_data_events()")
        self.connection._flush_output()
        print("self.connection._flush_output()")
        self.connection.close()


        return self.new_wb_list

