# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Huangye88Item(scrapy.Item):
    # define the fields for your item here like:
    co_name = scrapy.Field()
    co_mbno = scrapy.Field()
    co_info = scrapy.Field()
    co_addr = scrapy.Field()
    co_prod = scrapy.Field()
