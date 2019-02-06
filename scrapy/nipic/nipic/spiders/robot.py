# -*- coding: utf-8 -*-
import scrapy
from PIL import Image
from nipic.items import NipicItem
from scrapy.pipelines.images import ImagesPipeline

class RobotSpider(scrapy.Spider):
    name = 'robot'
    allowed_domains = ['nipic.com']
    start_urls = ['http://soso.nipic.com/?g=0&or=0&y=40']
    def parse(self, response):
        item = NipicItem()
        item['image_urls'] = response.xpath('//img[@class="lazy"]/@data-original').extract()
        yield item

        next_url = response.xpath('//a[@class="bg-png24 page-btn" and  @title="下一页"]/@href').extract_first()
        if next_url:
            next_url = 'http://soso.nipic.com' + next_url
            yield scrapy.Request(next_url, callback=self.parse)
