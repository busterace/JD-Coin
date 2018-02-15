#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

import time
from pathlib import Path

' a log module '

__author__ = 'busterace'


def get_today_day_time():
    return time.strftime('%Y%m%d', time.localtime())


def get_today_log_text():
    return get_log_text(get_today_day_time())


def get_log_text(day_time):
    log_file = Path(__file__).parent.joinpath("../log/" + get_log_file_name(day_time))
    return log_file.read_text()


def get_log_file_name(dayTime):
    return 'log' + dayTime + ".log"


if __name__ == '__main__':
    text = get_today_log_text()
    print(text)

log_format = '%(asctime)s %(name)s[%(module)s] %(levelname)s: %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)
logger = logging.getLogger()
file_handler = logging.FileHandler("../log/" + get_log_file_name(get_today_day_time()))
file_handler.formatter = logging.Formatter(log_format)
logger.addHandler(file_handler)