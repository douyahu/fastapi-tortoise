# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/13 10:57
@Auth ： 胡玉龙
@File ：responses.py
@IDE ：PyCharm
"""

class ResponseMessage():
    """
    API公共请求控制器, 无认证
    """

    @staticmethod
    def success(data=None, message=None, code=None):
        code = 0 if code is None else code
        data = data if data else None
        message = "success" if message is None else message
        return {"code": code, "message": message, "data": data}

    @staticmethod
    def fail(message=None, code=None, detail=None):
        code = 10000 if code is None else code
        message = "failed" if message is None else message
        detail = "" if detail is None else detail
        return {"code": code, "message": message, "detail": detail}