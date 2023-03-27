#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2023-03-12 15:45
# @Author  : estevam
# @Software: vscode

import os
import redis
import pymongo

LOGPATH = "/home/ubuntu/log" # os.environ.get('pspider_log')
PROXY = os.environ.get('psoider_proxy')

celery_broker = 'mongodb://127.0.0.1:27017/dev_broker'
redis_client = redis.Redis()
mongo_storage = pymongo.MongoClient()