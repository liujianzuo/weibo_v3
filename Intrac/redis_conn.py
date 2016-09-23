#!/usr/bin/env python
#_*_coding:utf-8_*_

from weibo import settings

import redis


def conn_redis(settings):
    Host = settings.REDIS_CONN['host']
    Port = settings.REDIS_CONN['port']
    pool = redis.ConnectionPool(host=Host, port=Port)

    r = redis.Redis(connection_pool=pool)
    return  r