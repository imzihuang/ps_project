# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from ps_db.unit import add_game_code

class PsValkyriePipeline(object):
    def __init__(self):
        self.down_folder = "down_file"


    def process_item(self, item, spider):
        #print item["ps_id"]
        print "-----------------------1111---------------"
        add_game_code(item['ps_id'])
        print "-----------------------2222---------------"
        return item

    def close_spider(self, spider):
        pass
        #self.filename.close()
