# -*- coding: utf-8 -*-
import scrapy


class WeixinSpider(scrapy.Spider):
    name = "weixin"
    allowed_domains = ["weixin.com"]
    start_urls = (
        'http://www.weixin.com/',
    )

    def parse(self, response):
        pass
