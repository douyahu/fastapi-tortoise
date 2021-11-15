# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：celery_app.py
@IDE ：PyCharm
"""

from celery import Celery

# 第一个参数Celery是当前模块的名称。这只是为了在__main__模块中定义任务时可以自动生成名称。
celery_app = Celery("celery_worker")

celery_app.config_from_object('backend.celery.celery_config', namespace='celery')
# celery_app.autodiscover_tasks(['backend.celery'])  # 自动发现任务



if __name__ == '__main__':
    celery_app.start()