# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""
from tortoise import Tortoise

from settings import TORTOISE_ORM


def tortoise_init(func):
    '''
    tortoise初始化装饰器
    :param func: 要装饰的函数名
    :return:装饰完的函数名
    '''

    async def wrap(*args, **kwargs):
        await Tortoise.init(config=TORTOISE_ORM)
        await Tortoise.generate_schemas()  # 在空数据库上生成架构
        result = await func(*args, **kwargs)
        return result

    return wrap
