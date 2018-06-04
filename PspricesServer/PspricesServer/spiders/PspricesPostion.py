# -*- coding: utf-8 -*-
import scrapy
from PspricesServer.items import PspricesserverItem


class PspricespostionSpider(scrapy.Spider):
    name = 'PspricesPostion'
    allowed_domains = ['eshop-prices.com']
    start_urls = ['http://eshop-prices.com/']

    def parse(self, response):
        for each in response.xpath('//tbody/tr'):
            gameurl = each.xpath("./th/a/@href").extract()[0]
            gamename = each.xpath("./th/a/text()").extract()[0]
            yield scrapy.Request(url=gameurl, meta={'gamename': gamename}, callback=self.game_parse)


    def game_parse(self, response):
        #print "start game---------------------------------------------:%s"%response.xpath('//div[@class="well"]/table/tr').extract()#.xpath('./tbody')
        gamename = response.meta['gamename']
        for each in response.xpath('//div[@class="well"]/table/tr'):
            if not each.xpath('./td').extract():
                continue
            # init
            item = PspricesserverItem()
            # 职位名称
            item['gamename'] = gamename
            item['countryname'] = each.xpath("./td[2]/text()").extract()[0]
            item['price'] = each.xpath("./td[4]/text()").extract()[0]
            print "-----------------:%s"%item
            yield  item