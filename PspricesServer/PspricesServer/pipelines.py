# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

down_folder = "down_file"

class PspricesserverPipeline(object):
    file_names = set()

    def process_item(self, item, spider):
        filename = item['gamename'].replace(" ", "_")
        filename += ".csv"
        if (not os.path.exists(down_folder)):
            os.makedirs(down_folder)

        if filename in self.file_names:
            fp = open(down_folder + '/' + filename, 'a')
        else:
            fp = open(down_folder + '/' + filename, 'w')
            fp.write(item['gamename']+"\n")
            self.file_names.add(filename)
        fp.write("%s, %s\n"%(item["countryname"], item["price"]))
        fp.close()

        return item
