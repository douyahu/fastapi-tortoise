# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/12 19:35
@Auth ： 胡玉龙
@File ：Test.py
@IDE ：PyCharm
"""

from tortoise import fields, Model
from tortoise.contrib.pydantic import pydantic_model_creator

from app.api.v1.validations.Test import TestValidator, TSValidator


class TestModel(Model):
    test = fields.IntField(null=False, description=f"Test value", validators=[TestValidator()])
    ts = fields.IntField(null=False, description=f"Epoch time", validators=[TSValidator()])


class UpdateTestModel(Model):
    ts = fields.IntField(null=False, description=f"Epoch time", validators=[TSValidator()])


# Pydantic schema
TestSchema = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}Schema")
TestSchemaCreate = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}SchemaCreate", exclude_readonly=True)
TestSchemaUpdate = pydantic_model_creator(UpdateTestModel, name=f"{UpdateTestModel.__name__}SchemaUpdate",
                                          exclude_readonly=True)
