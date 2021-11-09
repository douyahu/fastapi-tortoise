# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：producer.py
@IDE ：PyCharm
"""

# coding:utf-8

from .celery_tasks import add_sleep_2, add_sleep_10


def start_add_sleep_2():
    print("[*]Start function start_add_sleep_2")
    r = add_sleep_2.apply_async((2, 20000), queue='celery')  # 异步任务
    print(r.ready())
    # print(r.result)
    print(r.get())
    print(r.ready())
    # print(r.successful())
    print("[*]Done")


def start_add_sleep_10():
    print("[*]Start function start_add_sleep_60")  # 'e709795c-5ffd-4ed7-9d39-2a76b834dafb'
    r = add_sleep_10.delay(3, 3)
    print(r.result)
    print(r.get())
    print(r.ready())
    print("[*]Done")


if __name__ == "__main__":
    # start_add_sleep_2()
    start_add_sleep_10()
