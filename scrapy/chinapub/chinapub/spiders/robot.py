# -*- coding: utf-8 -*-
import scrapy
from chinapub.items import ChinapubItem


class RobotSpider(scrapy.Spider):
    name = 'robot'
    allowed_domains = ['china-pub.com']
    start_urls = ['http://product.china-pub.com/cache/browse2/59/1_2_59-05_0.html']

    def parse(self, response):
        item = ChinapubItem()
        for row in response.xpath('//div[@class="search_result"]/table'):
            item['bname'] = row.xpath('.//li[@class="result_name"]/a/text()').extract_first('not-found').strip()
            item['price'] = row.xpath('.//li[@class="result_book"]/ul/li[@class="book_dis"]/b/text()').extract_first('not-found').strip()
            yield item

        if response.xpath('//div[@class="pro_pag"]//tr/td[last()]/a/text()').extract_first().strip() == '下一页':
            next_page = response.xpath('//div[@class="pro_pag"]//tr/td[last()]/a/@href').extract_first().strip()
            next_page = 'http://product.china-pub.com' + next_page
            yield scrapy.Request(next_page, callback=self.parse)
