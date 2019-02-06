# -*- coding: utf-8 -*-
import scrapy, json, re
from PIL.Image import core
from fengniao.items import FengniaoItem
from scrapy.pipelines.images import ImagesPipeline

class RobotSpider(scrapy.Spider):
    name = 'robot'
    allowed_domains = ['fengniao.com']
    start_urls = ['https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=101&sort=0&page=1']

    def parse(self, response):
        item = FengniaoItem()
        rspn = json.loads(response.text)
        for each in rspn['content']:
            item['title'] = each['title'].strip()
            item['image'] = re.sub(r'\?.*$', '', each['image'])
            yield item
            

        for page in range(2, 20, 1):
            nxpg = 'https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=101&sort=0&page=' + str(page)
            yield scrapy.Request(nxpg, callback=self.parse)
