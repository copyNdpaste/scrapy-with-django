# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pydispatch import dispatcher
from scrapy import signals

from main.models import ScrapyItem


class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
        )

    def process_item(self, item, spider):
        scrapy_item = ScrapyItem()
        scrapy_item.unique_id = self.unique_id
        scrapy_item.title = item['title']
        scrapy_item.contents = item['contents']
        scrapy_item.published_date = item['published_date']
        scrapy_item.views = item['views']
        scrapy_item.recommends = item['recommends']
        scrapy_item.url = item['url']
        scrapy_item.category = item['category']

        scrapy_item.save()
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')
