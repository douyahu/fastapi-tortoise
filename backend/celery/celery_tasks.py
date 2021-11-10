from time import sleep

from .celery_app import celery_app



@celery_app.task(name='add_sleep_2', serializer='json')  # 定义default_task测试函数
def default_task(x, y) -> int:
    sleep(2)
    return x + y


@celery_app.task(name='music_task', serializer='json')  # 定义个music_task测试函数
def music_task(x, y) -> int:
    sleep(2)
    return x + y



@celery_app.task(name='video_task', serializer='json')  # 定义个video_task测试函数
def video_task(x, y) -> int:
    sleep(2)
    return x + y
