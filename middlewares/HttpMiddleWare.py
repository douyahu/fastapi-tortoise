# coding=utf-8
# @Version: python3.8.5
# @Software: PyCharm
# @File: responseMiddle.py
# @Company: 众安科技有限公司
# @Author: 胡玉龙
# @E-mail: huyulong@zhongan.io
# @Time: 2020年10月14日
import json
import logging
import re
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.v1.models.Log import Log
from utils.Logger import logger



def get_service_ip(request):
    ip = request.headers.get(
        'X-Forwarded-For', request.client.host)
    if ', ' in ip:
        ip = ip.split(', ')[0]
    return ip

async def get_log_dict(request):
    log = {
        'ip': get_service_ip(request),
        'status': True,
        'user_id': request.session["user"]["id"] if "user" in request.session else '',
        'desc': "",
        'requestMethod': request.method
    }
    return log


# 记录用户请求体信息
async def write_request_log(request):
    body = b''
    path = request.url.path
    method = request.method
    path_params = str(request.path_params)
    query_params = str(request.query_params)
    if await request.body():
        body = await request.body()
    info = "[Path:{0}] [Method:{1}] [Path_params:{2}] [Query_params:{3}] [Body:{4}]".format(path, method, path_params,
                                                                                            query_params, body)
    logger.info(info)


async def write_request_desc_log(request, log):
    '''
        根据请求url，写入对应的desc
    :param request:
    :param log:
    :return:
    '''
    pass


# 记录用户操作日志信息
async def write_response_log(request):
    log = await get_log_dict(request)
    try:
        if await request.body():
            log['requestBody'] = await request.body()
        await write_request_desc_log(request, log)

    except Exception as ex:
        logger.error('日志详情记录异常,异常原因:' + str(ex))
    # Log.create(**log)


async def write_request_method_log(method, log, request):
    '''
        根据请求方法，写入对应的desc
    :param method:
    :param log:
    :param request:
    :return:
    '''
    if await request.body():
        request_body = await request.body()
        request_json = json.loads(str(request_body, encoding='utf-8'))
        detail = ""
        for param in method['params']:
            if param['key'] in request_json:
                detail += '，' + param['value'] + "：" + str(request_json[param['key']])
        log['desc'] += detail


class ContextIncludedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            await write_request_log(request)
            response: Response = await original_route_handler(request)
            await write_response_log(request)
            return response

        return custom_route_handler


# Header中间件
class HeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return response


# 请求中间件
class RequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return response


# 返回中间件
class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return response
