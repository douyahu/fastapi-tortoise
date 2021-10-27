# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 14:37
@Auth ： 胡玉龙
@File ：__init__.py.py
@IDE ：PyCharm
"""

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.api.v1.routers import api_router
from common.exceptions import APIException
from common.responses import ResponseMessage as rsp
from middlewares.AuthenticationUser import AuthenticationUser
from settings import TORTOISE_ORM


def init_fastapi_app():
    '''
        创建fastapi APP
    :return: app
    '''
    middleware = [
        Middleware(
            ContextMiddleware,
            plugins=(
                plugins.RequestIdPlugin(),
                plugins.CorrelationIdPlugin()
            )
        ),
        # Middleware(
        #     SessionMiddleware, secret_key="6YJk0fjS4KjYPedeLOkLdjJimQRW3zZiwdrVFyedP2ygdOmys5yCjz76dCSvzwzE",
        #     session_cookie="tortoise"
        # ),
        Middleware(AuthenticationMiddleware, backend=AuthenticationUser()),

        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]

    app = FastAPI(middleware=middleware, title="Tortoise ORM FastAPI example")

    @app.exception_handler(APIException)
    async def validation_exception_handler(req: Request, ex: APIException):
        detail = str(ex)
        return JSONResponse(
            status_code=ex.status,
            content=rsp.fail(code=ex.code, message=ex.message, detail=ex.detail)
        )

    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,  # 如果数据库为空，则自动生成对应表单,生产环境不要开
        add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
    )

    app.include_router(api_router, responses={404: {"description": "Not found"}}, )

    return app

