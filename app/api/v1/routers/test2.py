# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/13 13:45
@Auth ： 胡玉龙
@File ：test2.py
@IDE ：PyCharm
"""
from fastapi import Depends
from fastapi_crudrouter import MemoryCRUDRouter, TortoiseCRUDRouter

from app.api.v1.models import TestSchema, TestSchemaCreate, TestSchemaUpdate, TestModel, User
from app.api.v1.routers import current_user

router = TortoiseCRUDRouter(
    schema=TestSchema,
    create_schema=TestSchemaCreate,
    update_schema=TestSchemaUpdate,
    db_model=TestModel,
    prefix="text2",  # 路由前缀
    delete_all_route=False
)




# router = MemoryCRUDRouter(schema=TestSchema, create_schema=TestSchemaCreate, prefix='text2')


# @router.get('')
# def overloaded_get_all():
#     return 'My overloaded route that returns all the items'


@router.get('/{item_id}')
def overloaded_get_one(user: User = Depends(current_user)):
    return 'My overloaded route that returns one item'
