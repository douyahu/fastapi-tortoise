# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:10
@Auth ： 胡玉龙
@File ：run.py.py
@IDE ：PyCharm
"""
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi_users.authentication import JWTAuthentication
from tortoise.contrib.fastapi import register_tortoise

from middleware import middleware
from settings import TORTOISE_ORM
from utils import env

app = FastAPI(middleware=middleware, title="Tortoise ORM FastAPI example")

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # 如果数据库为空，则自动生成对应表单,生产环境不要开
    add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)

jwt_authentication = JWTAuthentication(secret="SECRET", lifetime_seconds=3600)

from app.api.v1.routers import init_fastapi_router

init_fastapi_router(app)

# app.include_router(api_router, prefix='/api/v1', responses={404: {"description": "Not found"}}, )

if __name__ == '__main__':
    debug = env("DEBUG")
    reload = int(env("RELOAD"))
    port = int(env("PORT"))
    uvicorn.run(app='run:app', host="0.0.0.0", port=port, reload=reload, debug=debug)
