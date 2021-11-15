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
    r = default_task.delay(3, 3)  # delay方法仅允许方法传参，不允许其他参数传递
    print(r.ready())
    # print(r.result)
    # get方法等待任务完成
    # 防止worker异常，而引起get异常 ，设置propagate=False
    # 后端使用资源来存储和传输结果。为了确保资源被释放，您最终必须在调用任务后返回的每个实例上调用 get()或 forget()


    # forget()忘记这个任务的结果和它的父母
    print(r.get(propagate=False))
    print(r.result)
    print(r.backend)
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
    print(r.backend)
    print(r.get(propagate=False))
    print(r.ready())
    print("[*]Done")



def start_file_task():
    print("[*]Start function music_task")
    r = music_task.apply((1, 22222),
                               exhcange='media',
                               queue='music',
                               routing_key='media.music',
                               gnore_result=False)
    print(r.result)
    print(r.backend)
    print(r.get(propagate=False))
    print(r.ready())
    print("[*]Done")


def start_video_task():
    print("[*]Start function video_task")
    r = celery_app.send_task(name='video_task', queue='video', args=[56, 32211])
    print(r.result)
    print(r.get())
    print(r.ready())
    print("[*]Done")


if __name__ == "__main__":
    for i in range(100):
        start_default_task()
    # start_music_task()
    # start_video_task()
