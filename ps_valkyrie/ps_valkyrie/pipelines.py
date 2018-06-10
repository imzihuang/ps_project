# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class PsValkyriePipeline(object):
    def __init__(self):
        self.down_folder = "down_file"
        #self.filename = open("tencent.json", "w")

    def process_item(self, item, spider):
        #print item["ps_id"]
        filename = item['ps_id']
        filename += ".csv"
        if (not os.path.exists(self.down_folder)):
            os.makedirs(self.down_folder)

        fp = open(self.down_folder + '/' + filename, 'w')
        fp.write(item['body'] + "\n")
        fp.close()
        print item
        return item

    def close_spider(self, spider):
        pass
        #self.filename.close()
