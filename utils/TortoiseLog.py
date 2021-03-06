# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：TortoiseLog.py
@IDE ：PyCharm
"""

import logging
import sys

from utils import logging_level

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging_level)
sh.setFormatter(fmt)

# will print debug sql
tortoise_logger_db_client = logging.getLogger("tortoise.db_client")
tortoise_logger_db_client.setLevel(logging_level)
tortoise_logger_db_client.addHandler(sh)

tortoise_logger_tortoise = logging.getLogger("tortoise")
tortoise_logger_tortoise.setLevel(logging_level)
tortoise_logger_tortoise.addHandler(sh)
