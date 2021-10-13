# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/13 10:32
@Auth ： 胡玉龙
@File ：Test.py
@IDE ：PyCharm
"""

from tortoise.validators import Validator

from common.exceptions import APIException


class TestValidator(Validator):
    def __call__(self, value: int):
        if value != 123:
            raise APIException(code=10000, message='123', detail='123')


class TSValidator(Validator):
    def __call__(self, value: int):
        if value != 456:
            raise APIException(code=10000, message='123', detail='123')
