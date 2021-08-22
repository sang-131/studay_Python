# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl

class DoubanPipeline(object):
    def __init__(self):
        self.wb =openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['书名', '评论ID', '短评内容'])
    def process_item(self, item, spider):
        line = [item['book'], item['id'], item['comment']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('./豆瓣短评.xlsx')
        self.wb.close()