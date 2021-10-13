# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/13 10:45
@Auth ： 胡玉龙
@File ：exceptions.py
@IDE ：PyCharm
"""


class APIException(Exception):
    # 返回状态、返回码、返回中文信息，返回详细信息
    def __init__(self, code: int, message: str, status: int = 200, detail: str = ""):
        self.status = status
        self.code = code
        self.message = message
        self.detail = detail
