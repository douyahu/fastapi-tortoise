# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：LoggingRoute.py
@IDE ：PyCharm
"""
import json
import os
import time
import uuid
from datetime import datetime
from typing import Callable
from urllib.parse import parse_qs

from fastapi import HTTPException, Request, Response
from fastapi.routing import APIRoute
from user_agents import parse

from utils import logger


def get_service_ip(request):
    ip = request.headers.get(
        'X-Forwarded-For', request.client.host)
    if ', ' in ip:
        ip = ip.split(',')[0]
    return ip


class LoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                uuid_str = str(uuid.uuid4())
                header = dict(request.headers)
                if "uuid" in header.keys():
                    uuid_str = header["uuid"]
                user_agent = parse(request.headers["user-agent"])
                browser = user_agent.browser.version
                if len(browser) >= 2:
                    browser_major, browser_minor = browser[0], browser[1]
                else:
                    browser_major, browser_minor = 0, 0

                user_os = user_agent.os.version
                if len(user_os) >= 2:
                    os_major, os_minor = user_os[0], user_os[1]
                else:
                    os_major, os_minor = 0, 0

                # Request json
                body = await request.body()
                if len(body) != 0:
                    body = json.loads(body)
                else:
                    body = ""
                request_json = {
                    # "type": "request",
                    "uuid": uuid_str,
                    "env": os.environ.get("ENV"),
                    "region": os.environ.get("REGION"),
                    "name": os.environ.get("NAME"),
                    "ip": get_service_ip(request),
                    "method": request.method,
                    "useragent":
                        {
                            "family": user_agent.browser.family,
                            "major": browser_major,
                            "minor": browser_minor,
                            "patch": user_agent.browser.version_string,

                            "device": {
                                "family": user_agent.device.family,
                                "brand": user_agent.device.brand,
                                "model": user_agent.device.model,
                                "major": "0",
                                "minor": "0",
                                "patch": "0"
                            },
                            "os": {
                                "family": user_agent.os.family,
                                "major": os_major,
                                "minor": os_minor,
                                "patch": user_agent.os.version_string
                            },

                        },
                    "url": request.url.path,
                    "query": parse_qs(str(request.query_params)),
                    "body": body,
                    "content_length": request.get("content-length"),
                    "content_type": request.get("content-type"),
                    'time': f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'

                }
                start_time = time.time()
                response = await original_route_handler(request)
                process_time = (time.time() - start_time) * 1000
                formatted_process_time = '{0:.2f}'.format(process_time)

                metrics_json = {
                    # "type": "metrics",
                    "uuid": uuid_str,
                    "env": os.environ.get("ENV"),
                    "region": os.environ.get("REGION"),
                    "name": os.environ.get("NAME"),
                    "method": request.method,
                    "status_code": response.status_code,
                    "url": request.url.path,
                    "query": parse_qs(str(request.query_params)),
                    "content_length": response.headers["content-length"],
                    "content_type": response.headers["content-type"],
                    "latency": formatted_process_time,
                    "time": f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
                }

                if "health" not in request.url.path:
                    await wirte_request_log(request.user, request_json, metrics_json)
                return response
            except SyntaxError as exc:
                body = await request.body()
                if isinstance(exc, SyntaxError):
                    detail = {"errors": exc.msg, "body": body.decode("utf-8")}
                else:
                    detail = {"errors": str(exc.detail), "body": body.decode("utf-8")}
                logger.error(detail)
                raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler


async def wirte_request_log(user, request_json, metrics_json):
    '''
    记录所有router层的请求日志
    :param user: 操作人员id
    :param request_json: 请求json
    :param metrics_json: 响应json
    :return:
    '''
    from app.api.v1.models import LogModel
    log_dict = {**request_json, **metrics_json}
    log_dict['useragent'] = str(log_dict['useragent'])
    log_dict['query'] = str(log_dict['query'])
    log_dict['body'] = str(log_dict['body'])
    log_dict['user'] = user
    await LogModel.create(**log_dict)
    logger.debug("request:{data}".format(data=json.dumps(request_json)))
    logger.debug("response:{data}".format(data=json.dumps(metrics_json)))
