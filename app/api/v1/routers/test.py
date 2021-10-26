# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/12 19:40
@Auth ： 胡玉龙
@File ：test.py
@IDE ：PyCharm
"""
from fastapi_crudrouter import TortoiseCRUDRouter

from app.api.v1.models.Test import TestSchema, TestSchemaCreate, TestModel, TestSchemaUpdate
from middlewares.LoggingRoute import LoggingRoute

router = TortoiseCRUDRouter(
    schema=TestSchema,
    create_schema=TestSchemaCreate,
    update_schema=TestSchemaUpdate,
    db_model=TestModel,
    prefix="test",  # 路由前缀
    delete_all_route=False,
    route_class=LoggingRoute
)
