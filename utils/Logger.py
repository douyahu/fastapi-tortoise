# coding=utf-8
# @Version: python3.8.5
# @Software: PyCharm
# @File: logger.py
# @Company: 众安科技有限公司
# @Author: 胡玉龙
# @E-mail: huyulong@zhongan.io
# @Time: 2020年9月30日
import datetime
import os
import time
import zipfile

from loguru import logger

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 定位到log日志文件
log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)


# 一天一个日志文件
def should_rotate(message, file):
    filepath = os.path.abspath(file.name)
    creation = os.path.getctime(filepath)
    now = message.record["time"].timestamp()
    maxtime = 60 * 60 * 24  # 1 hour in seconds
    return now - creation > maxtime


# 超过7天的，按天压缩后存储
def logs_func(logs):
    day = datetime.datetime.today().date() - datetime.timedelta(days=3)
    file_list = []
    new_zip = zipfile.ZipFile(str(day) + ".zip", 'w')
    for log in logs:
        filepath = os.path.abspath(log)
        creation = os.path.getctime(filepath)
        if time.gmtime(time.time() - creation).tm_mday == 7:
            file_list.append(log)

    for tar in file_list:
        new_zip.write(tar)

    new_zip.close()

    for tar in file_list:
        filepath = os.path.abspath(tar)
        os.remove(filepath)


log_info_path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}.log')
logger.add(log_info_path, level="INFO", rotation=should_rotate, retention=logs_func, enqueue=True)
