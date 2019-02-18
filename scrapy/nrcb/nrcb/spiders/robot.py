# -*- coding: utf-8 -*-
import scrapy
from nrcb.items import NrcbItem

class RobotSpider(scrapy.Spider):
    name = 'robot'
    allowed_domains = ['nrcb99.com']
    start_urls = ['http://www.nrcb99.com/Videos/play/id/1']

    def parse(self, response):
        item = NrcbItem()
        item['title'] = response.xpath('//div[@class="play"]/h1[@id="h_title"]/text()').get('no-title').strip()
        item['video'] = response.xpath('//div[@class="video"]/video[@id="videoPlay"]/@src').get('no-video').strip()
        item['image'] = response.xpath('//div[@class="video"]/video[@id="videoPlay"]/@poster').get('no-video').strip()
        yield item

        for page in range(2, 1000):
            nxpg = 'http://www.nrcb99.com/Videos/play/id/' + str(page)
            yield scrapy.Request(nxpg, callback=self.parse)
