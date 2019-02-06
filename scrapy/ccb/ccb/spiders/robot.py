# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ccb.items import CcbItem


class RobotSpider(CrawlSpider):
    name = 'robot'
    allowed_domains = ['buy.ccb.com']
    start_urls = ['http://buy.ccb.com/searchproducts/pv_0_0_0_0.jhtml?query=*&catId=12003&selectCatId=12003']

    rules = (
        Rule(LinkExtractor(allow=r'searchproducts/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = CcbItem()
        for row in response.xpath('//div[@class="prolist_sr"]/dl'):
            item['pname'] = row.xpath('.//dd/ul/li/a[@class="prodname"]/text()').extract_first('not-found').strip()
            item['price'] = row.xpath('.//dd/ul/li/span[@class="fl"]/strong/text()').extract_first('not-found').strip()
            item['pshop'] = row.xpath('.//dd/ul/li/a[@style="max-width:168px;"]/text()').extract_first('not-found').strip()
            yield item
