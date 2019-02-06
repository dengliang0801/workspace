# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class MySQLPipeline(object):
    def open_spider(self, spider):
        db_host = spider.settings.get('MYSQL_HOST')
        db_port = spider.settings.get('MYSQL_PORT')
        db_name = spider.settings.get('MYSQL_NAME')
        db_user = spider.settings.get('MYSQL_USER')
        db_pswd = spider.settings.get('MYSQL_PSWD')
        db_char = spider.settings.get('MYSQL_CHAR')
        self.db_conn = MySQLdb.connect(host=db_host, port=db_port, db=db_name, user=db_user, passwd=db_pswd, charset=db_char)
        self.db_curs = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (item['co_name'], item['co_mbno'], item['co_addr'], item['co_prod'], item['co_info'])
        sql = 'INSERT INTO huangye88 VALUES (%s, %s, %s, %s, %s)'
        self.db_curs.execute(sql, values)


class Huangye88Pipeline(object):
    def process_item(self, item, spider):
        return item
