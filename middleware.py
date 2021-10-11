# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:17
@Auth ： 胡玉龙
@File ：middleware.py
@IDE ：PyCharm
"""
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware

middleware = [
    Middleware(
        ContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        )
    ),
    Middleware(
        SessionMiddleware, secret_key="6YJk0fjS4KjYPedeLOkLdjJimQRW3zZiwdrVFyedP2ygdOmys5yCjz76dCSvzwzE",
        session_cookie="tortoise"
    ),
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
]
