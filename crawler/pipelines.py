# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import SourceItem
from utils.django_api import save_source

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,SourceItem):
            save_source(item)
            return item
