# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:24
@Auth ： 胡玉龙
@File ：settings.py.py
@IDE ：PyCharm
"""
from utils import mysql_url

TORTOISE_ORM = {
    "connections": {"default": mysql_url},
    "apps": {
        "models": {
            # # 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "models": ["aerich.models", "app.api.v1.models"],
            "default_connection": "default",
        },
    },
}
