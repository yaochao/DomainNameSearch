# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import pymongo as pymongo
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
logger = logging.getLogger(__name__)


# 存储到Mongodb
class MongodbStorePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(
            settings['MONGO_HOST'],
            settings['MONGO_PORT']
        )
        self.db = self.client[settings['MONGO_DB']]
        self.collection = self.db[settings['MONGO_COLLECTION_XINNET']]

    def process_item(self, item, spider):
        print '---gg---', item['_id']
        try:
            self.collection.insert(dict(item))
        except Exception as e:
            logger.error(e)
            return item

    def __del__(self):
        self.collection.close()
        self.db.close()
        self.client.close()
