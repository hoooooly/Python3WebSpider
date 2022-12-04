# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymongo
from scrapy.exceptions import DropItem


class TextPipeline(object):

    def __init__(self):
        self.limit = 50

    # process_item 返回 item 或 DropItem 对象
    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit] + '...'
            return item
        else:
            return DropItem('Missing Text')


class MongoDBPipeline:
    def __init__(self, conn, database):
        self.conn = conn
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            conn=crawler.settings.get('MONGODB_CONNECTION_STRING'),
            database=crawler.settings.get('MONGODB_DATABASE')
        )

    def open_spider(self, spider):
        # 创建连接对象
        self.client = pymongo.MongoClient(self.conn)
        # 连接要用的使用的数据库
        self.db = self.client[self.database]

    def process_item(self, item, spider):
        # 设置使用表名称
        name = item.__class__.__name__
        # 默认item类名
        self.db[name].insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
