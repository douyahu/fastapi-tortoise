# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/9 15:10
@Auth ： 胡玉龙
@File ：run.py.py
@IDE ：PyCharm
"""

import typer
from tortoise import run_async

from backend.log import log_backend

typer_app = typer.Typer()


@typer_app.command(help='获取dn中的log日志')
def log_command():
    run_async(log_backend())


@typer_app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    typer_app()
