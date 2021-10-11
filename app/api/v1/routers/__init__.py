# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:05
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""
from fastapi import APIRouter

from app.api.v1.routers import health
from app.api.v1.services.User import get_user_manager


def include_health_router(app):
    health_router = APIRouter()
    health_router.include_router(health.router, prefix="/health", tags=["health"], )
    app.include_router(health_router, tags=["health"])


def get_fastapi_users():
    from run import jwt_authentication
    from fastapi_users import FastAPIUsers
    from app.api.v1.models import User, UserCreate, UserUpdate, UserDB

    fastapi_users = FastAPIUsers(
        get_user_manager,
        [jwt_authentication],
        User,
        UserCreate,
        UserUpdate,
        UserDB,
    )
    return fastapi_users


def include_auth_router(app, router=APIRouter()):
    from run import jwt_authentication
    fastapi_users = get_fastapi_users()
    router.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"], )
    router.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"], )
    router.include_router(fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"], )
    router.include_router(fastapi_users.get_verify_router(), prefix="/auth", tags=["auth"], )
    app.include_router(router, tags=["auth"])


def include_users_router(app, router=APIRouter()):
    fastapi_users = get_fastapi_users()
    router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"], )
    router.include_router(fastapi_users.get_users_router(requires_verification=True), prefix="/users", tags=["users"])
    app.include_router(router, tags=["users"])


def init_fastapi_router(app):
    include_health_router(app)
    include_auth_router(app)
    include_users_router(app)

# api_router = APIRouter()
# api_router.include_router(users.router, prefix="/users", tags=["users"])
