# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:06
@Auth ： 胡玉龙
@File ：users.py
@IDE ：PyCharm
"""
from fastapi import Depends, APIRouter

from app.api.v1.models import User
from app.api.v1.routers import fastapi_users

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

router = APIRouter()

router.include_router(fastapi_users.get_users_router())
router.include_router(fastapi_users.get_users_router(requires_verification=True))
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.get("/current-user")
async def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@router.get("/active-user")
async def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}"


@router.get("/active-verified-user")
def protected_route(user: User = Depends(current_active_verified_user)):
    return f"Hello, {user.email}"


@router.get("/active-super-user")
async def protected_route(user: User = Depends(current_superuser)):
    return f"Hello, {user.email}"
