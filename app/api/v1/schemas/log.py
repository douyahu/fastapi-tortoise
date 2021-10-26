# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：log.py
@IDE ：PyCharm
"""
from tortoise.contrib.pydantic import pydantic_model_creator

from app.api.v1.models import LogModel

LogSchema = pydantic_model_creator(LogModel, name=f"{LogModel.__name__}Schema")