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


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(models.BaseUserUpdate):
    pass


class UserModel(TortoiseBaseUserModel):
    class Meta:
        table = "User"


class UserDB(User, models.BaseUserDB, PydanticModel):
    class Config:
        orm_mode = True
        orig_model = UserModel


class OAuthAccount(TortoiseBaseOAuthAccountModel):
    user = fields.ForeignKeyField("models.UserModel", related_name="oauth_accounts")
