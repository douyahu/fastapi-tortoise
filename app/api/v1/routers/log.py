# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：log.py
@IDE ：PyCharm
"""
from fastapi_crudrouter import TortoiseCRUDRouter

from app.api.v1.models import LogModel
from app.api.v1.schemas.log import LogSchema
from middlewares.LoggingRoute import LoggingRoute

router = TortoiseCRUDRouter(
    schema=LogSchema,
    db_model=LogModel,
    prefix="log",  # 路由前缀
    route_class=LoggingRoute,
    create_route=False,
    update_route=False,
    delete_one_route=False,
    delete_all_route=False

)
