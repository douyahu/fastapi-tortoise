# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 15:36
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""

from utils.Env import get as env
from utils.Redis import Redis

mysql_url = env("MYSQL_URI")

# redis配置
redis_prefix = env("REDIS_PREFIX")
redis = Redis(
    env("REDIS_HOST"),
    env("REDIS_PORT"),
    env("REDIS_PASSWORD"),
    env("REDIS_DB"),
    int(env("REDIS_POOL_SIZE")),
    socket_connect_timeout=10,
    socket_keepalive=60,
    ssl=env("REDIS_SSL")
).conn
