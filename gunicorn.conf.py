#!usr/bin/env python
# encoding: utf-8
import multiprocessing

loglevel = "info"
port = 8080
# 监听端口
bind = '0.0.0.0:8080'

# 工作模式
worker_class = 'uvicorn.workers.UvicornWorker'

# 并行工作进程数
workers = multiprocessing.cpu_count()

# 设置守护进程
# daemon = True

errorlog = '/logs/gunicorn.error.log'  # 发生错误时log的路径
accesslog = '/logs/gunicorn.access.log'  # 正常时的log路径

# 设置最大并发量
worker_connections = 2000

keepalive = 15

timeout = 60
