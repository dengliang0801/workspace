# -*- coding: utf-8 -*-
import scrapy
from nrcb.items import NrcbItem

class RobotSpider(scrapy.Spider):
    name = 'robot'
    allowed_domains = ['nrcb99.com']
    start_urls = ['http://www.nrcb99.com/Videos/play/id/1']
    def parse(self, response):
        item = NrcbItem()
        title = response.xpath('//div[@class="play"]/h1[@id="h_title"]/text()').get('no-title').strip()
        video = response.xpath('//div[@class="video"]/video[@id="videoPlay"]/@src').get('no-video').strip()
        image = response.xpath('//div[@class="video"]/video[@id="videoPlay"]/@poster').get('no-video').strip()
#       item['image_urls'] = ['http://www.nrcb99.com' + image]
        item['image_urls'] = [response.urljoin(image)]
#       item['file_urls'] = ['http://www.nrcb99.com' + video]
        item['file_urls'] = [response.urljoin(video)]
        yield item

        for each in range(2, 100):
            page = 'http://www.nrcb99.com/Videos/play/id/' + str(each)
            yield scrapy.Request(page, callback=self.parse)
