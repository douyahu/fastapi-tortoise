# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：User.py
@IDE ：PyCharm
"""

from fastapi_users import models


class UserValidation(models.BaseUser):
    '''
    基本的字段和验证
    '''
    pass


class UserCreateValidation(models.BaseUserCreate):
    '''
    专用于用户注册
    '''
    pass


class UserUpdateValidation(models.BaseUserUpdate):
    '''专用于用户资料更新'''
    pass
