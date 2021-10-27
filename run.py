# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:10
@Auth ： 胡玉龙
@File ：run.py.py
@IDE ：PyCharm
"""
import time
from datetime import datetime

import typer
from tortoise import run_async

from backend.log import log_backend
from utils.Logger import logger

typer_app = typer.Typer()

interval = 5


@typer_app.command(help='单线程-定时获取db中的log日志')
def log():
    while True:
        logger.info("开始执行本轮脚本:{datatime}".format(datatime=datetime.now()))
        run_async(log_backend())
        logger.info("本轮脚本执行结束:{datatime}".format(datatime=datetime.now()))
        time.sleep(interval)


@typer_app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    typer_app()
