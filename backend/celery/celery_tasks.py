from time import sleep

from celery import current_task

from .celery_app import celery_app


@celery_app.task(acks_late=True)
def test_data_celery(word: str) -> str:
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i * 10})
    return f"test task return {word}"


@celery_app.task(name='add_sleep_2')  # 定义个测试函数，睡2秒，然后返回结果
def add_sleep_2(x, y) -> int:
    sleep(2)
    return x + y


@celery_app.task(name='add_sleep_10')  # 定义个测试函数，睡60秒，然后返回结果
def add_sleep_10(x, y) -> int:
    sleep(2)
    return x + y
