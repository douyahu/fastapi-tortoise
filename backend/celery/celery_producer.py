# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：producer.py
@IDE ：PyCharm
"""

# coding:utf-8
from backend.celery import celery_app
from backend.celery.celery_tasks import default_task, music_task


def start_default_task():
    print("[*]Start function default task")
    r = default_task.delay(3, 3)
    print(r.ready())
    # print(r.result)
    print(r.get())
    print(r.ready())
    # print(r.successful())
    print("[*]Done")


def start_music_task():
    '''
    gnore_result=True，不存储任务结果，节省资源和空间
    :return: None
    '''
    print("[*]Start function music_task")
    r = music_task.apply_async((1, 22222),
                               exhcange='media',
                               queue='music',
                               routing_key='media.music',
                               gnore_result=False)
    print(r.result)
    print(r.get())
    print(r.ready())
    print("[*]Done")


def start_video_task():
    print("[*]Start function video_task")
    r = celery_app.send_task(name='video_task', queue='video', args=[56, 311])
    print(r.result)
    print(r.get())
    print(r.ready())
    print("[*]Done")


if __name__ == "__main__":
    # start_default_task()
    # start_music_task()
    start_video_task()
