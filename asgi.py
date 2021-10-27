# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:10
@Auth ： 胡玉龙
@File ：run.py.py
@IDE ：PyCharm
"""
import uvicorn

from app import init_fastapi_app
from utils import env

app = init_fastapi_app()

if __name__ == '__main__':
    debug = env("DEBUG")
    reload = int(env("RELOAD"))
    port = int(env("PORT"))
    uvicorn.run(app='asgi:app', host="0.0.0.0", port=port, reload=reload, debug=debug, log_level="info")
