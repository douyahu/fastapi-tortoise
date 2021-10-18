# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:10
@Auth ： 胡玉龙
@File ：run.py.py
@IDE ：PyCharm
"""
import uvicorn as uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.api.v1.routers import api_router
from common.exceptions import APIException
from common.responses import ResponseMessage as rsp
from settings import TORTOISE_ORM
from utils import env

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

health_router = APIRouter()

# app.include_router(user_router)
app.include_router(api_router, responses={404: {"description": "Not found"}}, )

if __name__ == '__main__':
    debug = env("DEBUG")
    reload = int(env("RELOAD"))
    port = int(env("PORT"))
    uvicorn.run(app='run:app', host="0.0.0.0", port=port, reload=reload, debug=debug, log_level="info")
