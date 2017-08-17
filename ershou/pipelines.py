# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

db = pymongo.MongoClient()
xianyu = db.python.xianyu

class ErshouPipeline(object):
    def process_item(self, item, spider):
        return item

class WriteMongo(object):
    def process_item(self, item, spider):
        data = dict(item)
        xianyu.insert(data)
        return item
