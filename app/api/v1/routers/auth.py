# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:06
@Auth ： 胡玉龙
@File ：auth.py
@IDE ：PyCharm
"""

from fastapi import APIRouter

from app.api.v1.routers import fastapi_users, jwt_authentication

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/jwt", )
router.include_router(fastapi_users.get_register_router(), )
router.include_router(fastapi_users.get_reset_password_router(), )
router.include_router(fastapi_users.get_verify_router())
