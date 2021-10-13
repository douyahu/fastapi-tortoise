# coding=utf-8
# Software: PyCharm
# File: Log.py
# Company: 众安科技有限公司
# Author: 胡玉龙
# E-mail: huyulong@zhongan.io
# Time: 2021/5/19
from tortoise import fields
from tortoise.models import Model


class Log(Model):

    id = fields.IntField(pk=True, description='pk')
    user = fields.ForeignKeyField('models.UserModel', related_name='logs', description='操作用户')
    ip = fields.CharField(max_length=64, description='IP')
    desc = fields.CharField(max_length=255, description='描述')
    requestPath = fields.CharField(max_length=255, description='请求路径')
    requestMethod = fields.CharField(max_length=255, description='请求方法')
    requestBody = fields.TextField(description='请求体')
    status = fields.BooleanField(description='操作结果')

    def __str__(self):
        return self.user.name

    class Meta:
        table = "Log"
