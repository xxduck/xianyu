# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ershou.items import ErshouItem


class XianyuSpider(CrawlSpider):
    name = 'xianyu'
    # allowed_domains = ['https://s.2.taobao.com/list/list.htm',
    #                    'https://s.2.taobao.com']
    start_urls = ['https://s.2.taobao.com/list/list.htm']

    rules = (
        Rule(LinkExtractor(allow=r'https://s\.2\.taobao\.com/list/list\.htm/?.+\&ist=1'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ErshouItem()
        name = response.xpath('//div[@class="seller-nick"]/a/text()').extract()
        add = response.xpath('//div[@class="item-location"]/text()').extract()
        for k,v in zip(name,add):
            item['nick'] = k
            item['address'] = v
            return item
