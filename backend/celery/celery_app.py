# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：celery_app.py
@IDE ：PyCharm
"""

from celery import Celery

celery_app = Celery("celery_worker")
celery_app.config_from_object('backend.celery.celery_config',namespace='celery')
celery_app.autodiscover_tasks(['backend.celery'])  # 自动发现任务
# celery -A backend.celery.celery_app worker -l info -P eventlet -n win