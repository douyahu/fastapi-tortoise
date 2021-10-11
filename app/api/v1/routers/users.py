# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:06
@Auth ： 胡玉龙
@File ：users.py
@IDE ：PyCharm
"""
from fastapi import Depends, APIRouter

from app.api.v1.models import User
from run import fastapi_users

current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

router = APIRouter()


@router.get("/protected-route")
async def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@router.get("/active-protected-route")
async def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}"


@router.get("/super-protected-route")
async def protected_route(user: User = Depends(current_superuser)):
    return f"Hello, {user.email}"