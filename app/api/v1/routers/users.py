# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:06
@Auth ： 胡玉龙
@File ：users.py
@IDE ：PyCharm
"""
from fastapi import Depends, APIRouter

from app.api.v1.models import User
from app.api.v1.routers import fastapi_users, current_user, current_active_user, current_active_verified_user, \
    current_superuser
from middlewares.LoggingRoute import LoggingRoute

router = APIRouter(route_class=LoggingRoute)

router.include_router(fastapi_users.get_users_router(requires_verification=True))  # 是否需要用户认证


@router.get("/current-user", summary='获取个人信息')
async def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@router.get("/active-user", summary='是否为活跃用户')
async def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}"


@router.get("/active-verified-user", summary='是否为活跃的已登录用户')
def protected_route(user: User = Depends(current_active_verified_user)):
    return f"Hello, {user.email}"


@router.get("/active-super-user", summary='是否为活跃的超级用户')
async def protected_route(user: User = Depends(current_superuser)):
    return f"Hello, {user.email}"
