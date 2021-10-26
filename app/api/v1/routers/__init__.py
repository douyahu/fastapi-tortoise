# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:05
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""
from fastapi import APIRouter, Request, Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication, CookieAuthentication

from app.api.v1.models import User, UserCreate, UserUpdate, UserDB
from app.api.v1.services.User import get_user_manager

# jwt认证配置
jwt_authentication = JWTAuthentication(secret="SECRET", lifetime_seconds=3600, tokenUrl="auth/jwt/login")
# cookie认证配置
cookie_authentication = CookieAuthentication(secret="SECRET", lifetime_seconds=3600,)
fastapi_users = FastAPIUsers(get_user_manager, [jwt_authentication, cookie_authentication], User, UserCreate,
                             UserUpdate, UserDB, )
current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


async def get_enabled_backends(request: Request):
    """设置身份认证依赖启用."""
    if request.url.path == "/auth/jwt/login":
        return [jwt_authentication]
    else:
        return [cookie_authentication, jwt_authentication]


# 用户处于活跃状态，且需要通过cookie或jwt验证
current_active_user = fastapi_users.current_user(active=True, get_enabled_backends=get_enabled_backends)

from app.api.v1.routers import health, users, auth, test, test2

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(test.router, prefix="/api/v1", dependencies=[Depends(current_active_user)])
api_router.include_router(test2.router, prefix="/api/v1", )
