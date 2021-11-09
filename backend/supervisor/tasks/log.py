# # -*- coding: utf-8 -*-
# """
# @Auth ： 胡玉龙
# @File ：log.py
# @IDE ：PyCharm
# """
from app.api.v1.models import LogModel
from backend.supervisor.tasks import tortoise_init


@tortoise_init
async def log_backend():
    log = await LogModel.filter(id=1).first()
    print(log.uuid)
