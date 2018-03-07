#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: redis-tet.py
@time: 2018/3/7 15:51
"""
import redis
from rediscluster import StrictRedisCluster

serviceip = "192.168.42.133"
ports = [7000, 7001, 7002]
startup_nodes = [{"host": serviceip, "port": port} for port in ports]

def connRedisCluster():
    return StrictRedisCluster(startup_nodes=startup_nodes)

rdb = connRedisCluster()

rdb.set("youyou", "haha")
print rdb.get("hello"), 11111111
print rdb.get("shuainan"), 22222222
print rdb.get("youyou"), 333333333
