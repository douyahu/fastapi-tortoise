# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:06
@Auth ： 胡玉龙
@File ：auth.py
@IDE ：PyCharm
"""

from fastapi import APIRouter, Depends
from fastapi.openapi.models import Response

from app.api.v1.routers import fastapi_users, jwt_authentication, cookie_authentication
from middlewares.LoggingRoute import LoggingRoute

router = APIRouter(route_class=LoggingRoute)

# jwt登陆
router.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/jwt")

# cookie登陆、退出
router.include_router(fastapi_users.get_auth_router(cookie_authentication), prefix="/cookie")

# 身份认证
router.include_router(fastapi_users.get_verify_router())


# jwt token
@router.post("/jwt/refresh", summary='jwt-token刷新')
async def refresh_jwt(response: Response, user=Depends(fastapi_users.current_user(active=True))):
    return await jwt_authentication.get_login_response(user, response)
