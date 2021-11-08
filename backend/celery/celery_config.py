# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：celery_config.py
@IDE ：PyCharm
"""

enable_utc = False  # 使用UTC时间
timezone = 'Asia/Shanghai'  # 时区

accept_content = ['json']  # 允许的内容类型，非该类型的数据将被丢弃/序列化程序的白名单

# broker地址
broker_url = 'redis://:pwd@host:port/db1'
# 运行结果存储地址实例
result_backend = 'redis://:pwd@host:port/db2'  # 运行结果存储地址实例

broker_transport_options = {'max_retries': 5, 'visibility_timeout': 18000}  # 重试次数，和超时时间，如果第一次任务执行时代理不可用，生产者将不会永远重试

result_expires = 60 * 60 * 24  # 任务过期时间，为None永不过期

result_accept_content = ['json']  # 允许结果后端的内容类型/序列化器的白名单。

task_serializer = 'json'  # 要使用的默认序列化方法
task_track_started = True  # 精确显示任务的运行状况，长时间任务建议开启（pending, finished, waiting to be retried）

# 导入的任务模块
imports = []

# 和import相同，只是用于加载特殊模块，以示区分
include = []

# 在每个任务执行之前，指示工作人员检查此任务是否是重复
# 消息重复数据删除仅发生在具有相同标识符、启用延迟确认、由消息代理重新交付且其状态SUCCESS在结果后端中的任务。
# 为了避免查询溢出结果后端，在查询结果后端之前检查成功执行任务的本地缓存，以防任务已由接收任务的同一个工作人员成功执行。
# 存储结果不是持久的，则忽略此设置。
worker_deduplicate_successful_tasks = False

# CPU 内核数
worker_concurrency = 4

# 一次预取的消息数乘以并发进程数。默认值为 4（每个进程 4 条消息）。
# 但是，默认设置通常是一个不错的选择
# 如果您有很长的运行任务在队列中等待并且您必须启动工作程序，请注意第一个启动的工作程序将收到四倍于最初的消息数。
# 因此，任务可能不会公平地分配给工人。
worker_prefetch_multiplier = 4

# worker异常退出之前的等待时间
worker_lost_wait = 10

# 池里的工作进程在被新任务替换之前可以执行的最大任务数。默认是没有限制。
# worker_max_tasks_per_child

# 如果单个worker超过此内存限制，则该worker将被退出，并且被新worker进行替换。
# worker_max_memory_per_child = 12000

# worker工作频率速率限制，默认不限制
worker_disable_rate_limits = False

# 用于存储工作状态（如已撤销的任务）的文件的名称，状态数据库的路径
worker_state_db = None

# 设置 ETA 调度程序在重新检查调度之间可以休眠的最长时间（以秒为单位）
worker_timer_precision = 1

# 指定是否启用worker的远程控制。
worker_enable_remote_control = True

# 等待新worker进程启动时的超时时间
worker_proc_alive_timeout = 4.0

# 终止所有长时间运行的任务，并在连接丢失时启用延迟确认
worker_cancel_long_running_tasks_on_connection_loss = False

# 发送与任务相关的事件，以便可以使用花等工具监控任务 设置 workers-E参数的默认值 。默认禁用
# worker_send_task_events

# task-sent将为每个任务发送一个事件，以便可以在任务被工作人员使用之前对其进行跟踪
# task_send_sent_event=False

# 发送到监视器客户端事件队列的消息被删除时的消息到期时间，amqp
# event_queue_ttl

# 在监视器客户端事件队列将被删除 ( x-expires)之后的以秒为单位的到期时间 (int/float )。
# event_queue_expires

# 用于事件接收器队列名称的前缀。
# event_queue_prefix

# 管道名称
# event_exchange
# 消息序列化格式
# event_serializer


#######远程控制命令配置#######
# 如果使用默认值 300 秒，这意味着如果发送了远程控制命令并且在 300 秒内没有工作人员接听，则该命令将被丢弃
control_queue_ttl = 300
# 从代理中删除未使用的远程控制命令队列之前的时间
control_queue_expires = 10.0
# 控制命令交换的名称'
control_exchange = 'celery'

#######日志#######
worker_hijack_root_logger = False  # 是否使用默认的celery日志处理程序，为False则需自定义
worker_log_color = True  # 日志是否要启用颜色
worker_log_format = "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"  # 日志格式
worker_task_log_format = "[%(asctime)s: %(levelname)s/%(processName)s]%(task_name)s[%(task_id)s]: %(message)s"
worker_redirect_stdouts = True  # 将进程的屏幕、文件日志通过logging输出
worker_redirect_stdouts_level = 'INFO'  # 日志级别(DEBUG，INFO，WARNING， ERROR，或CRITICAL)

#######安全#######
# 包含使用消息签名时用于签名消息的私钥的文件的相对或绝对路径
security_key = None
security_cert_store = None
security_certificate = None
security_digest = None

############自定义组件类（高级）##############
# 工作程序使用的池类的名称
worker_pool = 'prefork'

# 如果启用，可以使用pool_restart远程控制命令重新启动工作池
worker_pool_restarts = False

# 要使用的自动计数器程序类的名称。
# worker_autoscaler

# worker使用的消费者类的名称。
# worker_consumer

# 工作程序使用的 ETA 调度程序类的名称。默认为或由池实现设置
# worker_timer


############定时任务##############
beat_schedule = {}

# 默认调度程序类
# beat_scheduler =

# 存储周期性任务的上次运行时间的文件的名称。可以是相对或绝对路径，但请注意后缀.db可能会附加到文件名
# beat_schedule_filename =

# 在发出另一个数据库同步之前可以调用的周期性任务数。
# 值 0（默认值）表示基于时间同步 - 由 scheduler.sync_every 确定的默认值为 3 分钟。
# 如果设置为 1，beat 将在每个任务消息发送后调用同步。
# beat_sync_every =

# beat检查计划之间可以休眠的最大秒数
# beat_max_loop_interval =

# 用于消费和生产的代理连接。
# broker_read_url = 'amqp://user:pass@broker.example.com:56721'
# broker_write_url = 'amqp://user:pass@broker.example.com:56722'
