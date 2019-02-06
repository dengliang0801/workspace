# -*- coding: utf-8 -*-
import scrapy, json, re
from PIL.Image import core
from fengniao.items import FengniaoItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline

class RobotSpider(scrapy.Spider):
    name = 'robot'
    allowed_domains = ['fengniao.com']
    start_urls = ['https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=101&sort=0&page=1']

    def parse(self, response):
        urls = []
        item = FengniaoItem()
        rspn = json.loads(response.text)
        for each in rspn['content']:
##          rspn['content'][1].get('image').split('?')[0]
##          item['image_urls'].append(each.get('image').split('?')[0])
            urls.append(each['image'].split('?')[0])
        item['image_urls'] = urls
        yield item

        for page in range(2, 20, 1):
            nxpg = 'https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=101&sort=0&page=' + str(page)
            yield scrapy.Request(nxpg, callback=self.parse)
