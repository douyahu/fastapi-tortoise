# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:05
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""

from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication, CookieAuthentication

from app.api.v1.models import User, UserCreate, UserUpdate, UserDB
from app.api.v1.services.User import get_user_manager

jwt_authentication = JWTAuthentication(secret="SECRET", lifetime_seconds=3600)
cookie_authentication = CookieAuthentication(secret="SECRET", lifetime_seconds=3600)
fastapi_users = FastAPIUsers(get_user_manager, [jwt_authentication], User, UserCreate, UserUpdate, UserDB, )

from app.api.v1.routers import health, users, auth

user_router = APIRouter()
user_router.include_router(health.router, prefix="/health", tags=["health"])
user_router.include_router(users.router, prefix="/users", tags=["users"])
user_router.include_router(auth.router, prefix="/auth", tags=["auth"])

api_v1_router = APIRouter()
