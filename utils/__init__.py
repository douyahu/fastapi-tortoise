# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 15:36
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""
import redis as redis
from loguru import logger

from utils.Email import EmailService
from utils.Env import get as env
from utils.Logger import log_info_path, should_rotate, logs_func

secret = env("SECRET")
lifetime_seconds = int(env("LIFETIME_SECONDS"))
logging_level = env("LOGGING_LEVEL")

mysql_host = env("MYSQL_HOST")
mysql_port = env("MYSQL_PORT")
mysql_database = env("MYSQL_DATABASE")
mysql_username = env("MYSQL_USERNAME")
mysql_password = env("MYSQL_PASSWORD")
mysql_url = env("MYSQL_URI")

# redis配置
redis_prefix = env("REDIS_PREFIX")
redis_pool = redis.ConnectionPool(host=env("REDIS_HOST"),
                                  port=env("REDIS_PORT"),
                                  db=env("REDIS_DB"),
                                  password=env("REDIS_PASSWORD"),
                                  socket_connect_timeout=10,
                                  socket_keepalive=60,
                                  )
redis_client = redis.StrictRedis(connection_pool=redis_pool)

# 邮件
email_service = EmailService(env("EMAIL_SERVER"),
                             env("EMAIL_PORT"),
                             env("EMAIL_USE_SSL"),
                             env("EMAIL_USERNAME"),
                             env("EMAIL_PASSWORD"),
                             env("EMAIL_DEFAULT_SENDER"))

# logger配置
logger.add(log_info_path, level="DEBUG", rotation=should_rotate, retention=logs_func, enqueue=True)

# tortoise log日志
from utils.TortoiseLog import tortoise_logger_db_client, sh, tortoise_logger_tortoise

tortoise_logger_db_client.addHandler(sh)
# tortoise_logger_tortoise.addHandler(sh)
