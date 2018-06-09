# -*- coding: utf-8 -*-
import scrapy
from ps_valkyrie.items import PsValkyrieItem


class ValkyrieSpider(scrapy.Spider):
    name = 'valkyrie'
    allowed_domains = ['store.playstation.com']
    _page = 1
    _ps_dic = {"lang":"en", "region":"hk", "page":_page}
    _url = 'https://store.playstation.com/%(lang)s-%(region)s/grid/STORE-MSF86012-PS4TITLES/%(page)d'
    start_urls = [_url % _ps_dic]
    _num = 0

    def parse(self, response):
        # grid-cell grid-cell--game
        _lang = self._ps_dic.get("lang", "en")
        _region = self._ps_dic.get("region", "hk")
        for each in response.xpath('//div[@class="grid-cell grid-cell--game"]'):
            _href = each.xpath('./a/@href').extract()[0]
            _valkyrie_url = "https://store.playstation.com/valkyrie-api/%(lang)s/%(region)s/19/resolve/%(ps_id)s"%{
                "lang": _lang,
                "region": _region,
                "ps_id": _href.rpartition("/")[-1]
            }
            _meta = {
                "lang": _lang,
                "region": _region,
                "ps_id": _href.rpartition("/")[-1]
            }
            yield scrapy.Request(url=_valkyrie_url, meta=_meta, callback=self.valkyrie_parse)

        #if self._page < 52:
        if self._page < 2:
            self._page += 1
        self._ps_dic.update({"page": self._page})
        yield scrapy.Request(url=self._url % self._ps_dic, callback=self.parse)


    def valkyrie_parse(self, response):
        _meta = response.meta
        item = PsValkyrieItem()
        item["lang"] = _meta.get("lang", "en")
        item["region"] = _meta.get("region", "hk")
        item["ps_id"] = _meta.get("ps_id", "en")
        item["body"] = response.body

        self._num += 1
        print self._num

        yield item