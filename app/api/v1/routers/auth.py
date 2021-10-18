# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:06
@Auth ： 胡玉龙
@File ：auth.py
@IDE ：PyCharm
"""

from fastapi import APIRouter

from app.api.v1.routers import fastapi_users, jwt_authentication

router = APIRouter()

# jwt登陆
router.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/jwt")

# 注册
router.include_router(fastapi_users.get_register_router(), )

# 重置密码
router.include_router(fastapi_users.get_reset_password_router(), )

#
router.include_router(fastapi_users.get_verify_router())
