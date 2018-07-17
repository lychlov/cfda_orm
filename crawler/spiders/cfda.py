# -*- coding: utf-8 -*-
import json

import scrapy

from crawler.items import SourceItem
from utils import get_source


class CfdaSpider(scrapy.Spider):
    name = 'cfda'
    allowed_domains = ['sfda.gov.cn', '223.105.3.139/']
    start_urls = ['http://baidu.com/']
    splash_api_1 = 'http://223.105.3.139:8050/execute?wait=0.5&images=1&expand=1&timeout=90.0&url=http%3A%2F%2Fsq.sfda.gov.cn%2Fdatasearch%2Fschedule%2Fsearch.jsp%3FtableId%3D43%26tableName%3DTABLE43%26columnName%3DCOLUMN464%2CCOLUMN475%26title1%3D%25E8%258D%25AF%25E5%2593%2581%25E6%25B3%25A8%25E5%2586%258C%25E8%25BF%259B%25E5%25BA%25A6%25E6%259F%25A5%25E8%25AF%25A2&lua_source=function+main%28splash%2C+args%29%0D%0A++function+focus%28sel%29%0D%0A++++++++splash%3Aselect%28sel%29%3Afocus%28%29%0D%0A++end%0D%0A++assert%28splash%3Ago%28args.url%29%29%0D%0A++assert%28splash%3Await%281%29%29%0D%0A++focus%28%27input%5Bid%3Dcolval%5D%27%29%0D%0A++%0D%0A++splash%3Asend_keys%28%22'
    splash_api_2 = '%22%29%0D%0A++assert%28splash%3Await%281%29%29%0D%0A++focus%28%27input%5Bid%3Dinput1%5D%27%29%0D%0A++%0D%0A++local+button+%3D+splash%3Aselect%28%27%23testAjax%27%29%0D%0A%09button%3Amouse_click%28%29%0D%0A++assert%28splash%3Await%281%29%29%0D%0A%0D%0A++local+form+%3D+splash%3Aselect%28%27form%27%29%0D%0A%09%0D%0A++return+assert%28form%3Aform_values%28%29%29%0D%0A%0D%0Aend'

    target_url = 'http://sq.cfda.gov.cn/datasearch/schedule/search.jsp?tableId=43&tableName=TABLE43&columnName=COLUMN464,COLUMN475&title1=%E8%8D%AF%E5%93%81%E6%B3%A8%E5%86%8C%E8%BF%9B%E5%BA%A6%E6%9F%A5%E8%AF%A2&code=%s&ik=%s'

    def start_requests(self):
        dataset = get_source()
        for data in dataset:
            if data.code == "":
                splash_url = self.splash_api_1 + data.id + self.splash_api_2
                yield scrapy.Request(url=splash_url, callback=self.parse)

    def parse(self, response):
        json_set = json.loads(response.body.decode('utf-8'))
        target = "http://sq.cfda.gov.cn/datasearch/schedule/search.jsp?tableId=43&tableName=TABLE43&columnName=COLUMN464,COLUMN475&title1=%E8%8D%AF%E5%93%81%E6%B3%A8%E5%86%8C%E8%BF%9B%E5%BA%A6%E6%9F%A5%E8%AF%A2&"
        target += "code=%s&ik=%s" % (json_set.get('code'), json_set.get('ik'))
        # target = "%s%s" %(json_set.get('code'),json_set.get('ik'))
        if json_set.get('code', '') != '':
            item = SourceItem()
            item['id'] = json_set.get('colval')
            item['code'] = json_set.get('code')
            item['ik'] = json_set.get('ik')
            yield item
            # yield scrapy.Request(url=target, callback=self.parse_target)
        pass

    def parse_target(self, response):

        pass
