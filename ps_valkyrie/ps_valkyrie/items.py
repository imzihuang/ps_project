# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PsValkyrieItem(scrapy.Item):
    # define the fields for your item here like:
    lang = scrapy.Field()
    region = scrapy.Field()
    ps_id = scrapy.Field()
    body = scrapy.Field()
