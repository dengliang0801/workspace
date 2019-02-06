# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xicidaili.items import XicidailiItem


class RobotSpider(CrawlSpider):
    name = 'robot'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1', 'https://www.xicidaili.com/wn/1',]

    rules = (
        Rule(LinkExtractor(allow=r'^https://www.xicidaili.com/nn/[1-9]?$'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'^https://www.xicidaili.com/wn/[1-9]?$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = XicidailiItem()
        host_list = response.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[2]/text()').extract()
        port_list = response.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[3]/text()').extract()
        type_list = response.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[6]/text()').extract()
        rows = response.xpath('//table[@id="ip_list"]/tr[@class="odd" or @class=""]')
        for line in rows:
            proxy_host = line.xpath('./td[2]/text()').extract_first('not-found').strip()
            proxy_port = line.xpath('./td[3]/text()').extract_first('not-found').strip()
            proxy_type = line.xpath('./td[6]/text()').extract_first('not-found').strip().lower()
            proxy_dict = {proxy_type: proxy_host+':'+proxy_port}
            item['proxy_info'] = proxy_type + '://' + proxy_host + ':' + proxy_port
            try:
                rsp = request.get('http://www.baidu.com/', proxies=proxy_dict, timeout=5)
                print(rsp.status_code)
                if rsp.status_code == 200:
                    print("成功: " + item['proxy_info'])
                    yield item
            except:
                print("失败: " + item['proxy_info'])
