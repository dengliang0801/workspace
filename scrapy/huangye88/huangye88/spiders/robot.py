# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from huangye88.items import Huangye88Item


class RobotSpider(CrawlSpider):
    name = 'robot'
    allowed_domains = ['huangye88.com']
    start_urls = ['http://b2b.huangye88.com/guangzhou/qichegaizhuang3340/']

    rules = (
        Rule(LinkExtractor(allow=r'http://b2b.huangye88.com/guangzhou/qichegaizhuang3340/pn\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = Huangye88Item()
        rows = response.xpath('//div[@class="mach_list2"]//dl')
        for ridx in rows:
            item['co_name'] = ridx.xpath('./dt/h4/a/text()').get('暂无数据').strip()
            item['co_mbno'] = ridx.xpath('./dt/span/a/text()').get('暂无数据').strip()
            item['co_info'] = ridx.xpath('./dd[@class="txt"]/text()').get('暂无数据').strip()
            item['co_addr'] = ridx.xpath('./dd/span[@itemprop="address"]/text()').get('暂无数据').strip()
            item['co_prod'] = ridx.xpath('./dd[last()]/text()[last()]').get('暂无数据').strip()
            yield item
