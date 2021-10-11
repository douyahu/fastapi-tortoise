# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 11:39
@Auth ： 胡玉龙
@File ：health.py
@IDE ：PyCharm
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health():
    return 'success'
