# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:05
@Auth ： 胡玉龙
@File ：User.py
@IDE ：PyCharm
"""
from fastapi_users import models
from fastapi_users.db import TortoiseBaseUserModel
from fastapi_users_db_tortoise import TortoiseBaseOAuthAccountModel
from tortoise import fields
from tortoise.contrib.pydantic import PydanticModel

from app.api.v1.validations.User import UserValidation


class UserModel(TortoiseBaseUserModel):
    '''数据库模型'''

    class Meta:
        table = "User"


class UserDB(UserValidation, models.BaseUserDB, PydanticModel):
    '''模型映射'''

    class Config:
        orm_mode = True
        orig_model = UserModel

