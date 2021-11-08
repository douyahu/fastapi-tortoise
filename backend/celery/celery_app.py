# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：celery_app.py
@IDE ：PyCharm
"""

from celery import Celery

celery_app = Celery("celery_worker")
celery_app.config_from_object('celery_demo.celery_config',namespace='celery')
celery_app.autodiscover_tasks(['celery_demo'])  # 自动发现任务
