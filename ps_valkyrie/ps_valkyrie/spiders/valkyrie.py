# -*- coding: utf-8 -*-
import scrapy
import json
from ps_valkyrie.items import PsValkyrieItem
from ps_valkyrie.unit import unit_data

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
            item = PsValkyrieItem()
            item["ps_id"] = _href.rpartition("/")[-1]
            yield item
            #yield scrapy.Request(url=_valkyrie_url, meta=_meta, callback=self.valkyrie_parse)

        if self._page < 52:
            self._page += 1
        self._ps_dic.update({"page": self._page})
        yield scrapy.Request(url=self._url % self._ps_dic, callback=self.parse)

    def valkyrie_parse(self, response):
        _meta = response.meta
        item = PsValkyrieItem()
        item["lang"] = _meta.get("lang", "en")
        item["region"] = _meta.get("region", "hk")
        item["ps_id"] = _meta.get("ps_id", "")

        data = unit_data(json.loads(response.body))
        item["content_rating"] = data.get("content_rating")
        item["file_size"] = data.get("file_size")
        item["game_content_type"] = data.get("game_content_type")
        item["genres"] = data.get("genres")
        item["long_description"] = data.get("long_description")
        item["media_list"] =  data.get("media_list")
        item["name"] = data.get("name")
        item["parent"] = data.get("parent")
        item["platforms"] = data.get("platforms")
        item["plus_reward_description"] = data.get("plus_reward_description")
        item["provide_name"] = data.get("provide_name")
        item["ps_camera_compatibility"] = data.get("ps_camera_compatibility")
        item["ps_vr_compatibility"] = data.get("ps_vr_compatibility")
        item["release_date"] = data.get("release_date")
        item["skus"] = {"data": data.get("skus")}
        item["star_rating"] = data.get("star_rating")
        item["subtitle_language_codes"] = data.get("subtitle_language_codes")
        item["voice_language_codes"] = data.get("voice_language_codes")
        item["thumbnail_url_base"] = data.get("thumbnail_url_base")
        item["upsell_info"] = data.get("upsell_info")

        yield item

