import logging


logger = logging.getLogger('jobs')

from .bean import Bean
from .bean_app import BeanApp
from .bean_jr import SignJR
from .daka_app import DakaApp
from .data_station import DataStation

__all__ = ['jobs_all', 'logger']

jobs_mobile = [DakaApp, BeanApp, DataStation]
jobs_web = [Bean, SignJR]
jobs_all = jobs_mobile + jobs_web

