# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAppItem(scrapy.Item):
    unique_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    contents = scrapy.Field()
    published_date = scrapy.Field()
    views = scrapy.Field()
    recommends = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    pass
