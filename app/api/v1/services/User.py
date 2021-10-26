# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 18:12
@Auth ： 胡玉龙
@File ：User.py
@IDE ：PyCharm
"""
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from fastapi_users_db_tortoise import TortoiseUserDatabase

from app.api.v1.models import UserDB, UserModel
from app.api.v1.validations.User import UserCreateValidation

SECRET = "SECRET"


class UserManager(BaseUserManager[UserCreateValidation, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_verify(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has been verified")

    async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
            self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")



# 数据库适配器
def get_user_db():
    yield TortoiseUserDatabase(UserDB, UserModel)


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
