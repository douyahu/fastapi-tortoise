# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/11 15:36
@Auth ： 胡玉龙
@File ：Env.py
@IDE ：PyCharm
"""
import io
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_config_by_env(env="DEPLOY_ENV"):
    """读取环境变量，默认读取dev"""
    value = os.environ.get(env, 'dev.env')
    if value == 'loc':
        return "loc.env"
    elif value == 'test':
        return "test.env"
    elif value == 'pre':
        return "pre.env"
    elif value == 'prd':
        return "prd.env"
    elif value == 'pub':
        return "pub.env"
    else:
        return "dev.env"


def file_to_json(file_path):
    """读取本地配置文件"""
    data = {}
    with io.open(file_path, encoding="utf-8") as f:
        for line in f.readlines():
            content = line.strip()
            if content != "":
                arr = content.split("=")
                data[arr[0].strip()] = ("=".join(arr[1:])).strip()
    return data


def get_env_path():
    env_path = os.path.join(BASE_DIR, get_config_by_env("DEPLOY_ENV"))
    return env_path


config = file_to_json(get_env_path())


def get(name, default=None):
    if name not in config:
        return default
    if config[name].lower() == "true":
        return True
    if config[name].lower() == "false":
        return False
    return config[name]
