# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisCrawlSpider,RedisSpider



class McSpider(RedisCrawlSpider):
    name = 'mc'
    allowed_domains = ['yunshanmeicai.com']
    # start_urls = ['https://online.yunshanmeicai.com/mall/api/search/getsearchlistbyc2']
    redis_key = "mc"
    def parse(self, response):

        print(response.text)
        pass
