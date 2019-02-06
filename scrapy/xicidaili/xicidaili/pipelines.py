# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XicidailiPipeline(object):
    def __init__(self):
        self.file = open('xici_output.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = item['proxy_info'] + '\n'
        self.file.write(text)
        return item

    def close_spider(self, spider):
        self.file.close()
