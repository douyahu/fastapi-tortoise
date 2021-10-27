# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 15:36
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""

from loguru import logger

from utils.Env import get as env
from utils.Logger import log_info_path, should_rotate, logs_func
from utils.Redis import Redis
from utils.TortoiseLog import tortoise_logger_db_client, sh, tortoise_logger_tortoise

mysql_host = env("MYSQL_HOST")
mysql_port = env("MYSQL_PORT")
mysql_database = env("MYSQL_DATABASE")
mysql_username = env("MYSQL_USERNAME")
mysql_password = env("MYSQL_PASSWORD")
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

# logger配置
logger.add(log_info_path, level="DEBUG", rotation=should_rotate, retention=logs_func, enqueue=True)

# tortoise log日志
tortoise_logger_db_client.addHandler(sh)
# tortoise_logger_tortoise.addHandler(sh)
