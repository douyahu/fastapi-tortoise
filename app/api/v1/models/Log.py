# coding=utf-8
# Software: PyCharm
# File: Log.py
# Company: 众安科技有限公司
# Author: 胡玉龙
# E-mail: huyulong@zhongan.io
# Time: 2021/5/19
from tortoise import fields
from tortoise.models import Model


class LogModel(Model):
    '''
    日志模型
    '''
    id = fields.IntField(pk=True, description='pk')
    user = fields.ForeignKeyField('models.UserModel', related_name='logs', description='操作用户', null=True, )
    ip = fields.CharField(null=True, max_length=128, description='IP')
    # type = fields.CharField(max_length=64, description='类型')
    uuid = fields.CharField(max_length=64, description='uuid')
    env = fields.CharField(null=True, max_length=64, description='env')
    region = fields.CharField(null=True, max_length=64, description='区域')
    name = fields.CharField(null=True, max_length=64, description='名称')
    method = fields.CharField(max_length=20, description='方法')
    useragent = fields.TextField(null=True, description='user_agent')
    url = fields.CharField(max_length=255, description='请求URL')
    query = fields.CharField(null=True, max_length=255, description='Query参数')
    body = fields.TextField(null=True, description='请求体')
    content_length = fields.IntField(null=True, description='content长度')
    content_type = fields.CharField(null=True, max_length=32, description='content类型')
    latency = fields.CharField(null=True, max_length=255, description='延迟')
    time = fields.DatetimeField(description='时间')
    status_code = fields.IntField(max_length=255, description='响应状态')
    desc = fields.CharField(null=True, max_length=255, description='描述')

    def __str__(self):
        return self.user.name

    class Meta:
        table = "Log"
