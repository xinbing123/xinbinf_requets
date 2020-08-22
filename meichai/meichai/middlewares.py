# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
import json
from scrapy import signals
import hashlib
import random
import time
import requests

from db.db_redis import SALE_C1_IS,redis_cli




class MeichaiSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MeichaiDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        url = request.url
        formdata = {
            "tickets": "jwt:eyJhbGciOiJSUzI1NiJ9.eyJpZCI6IjIwMzg5OTc5IiwianRpIjoiOTYyYmYwNjc5NDY4MTEzOWI5NDk5Y2I2NGNmZGNkNDMiLCJpYXQiOjE1NTk1Njg2MDY2MzJ9.t0csg4r-X_AVcxP0zg_uzACRtAkau10a87fHE8-O8E4fGqdC5e3QVbYFin_zFN70C_t3byxmU7PXpI6Ep5FcewAYV0R6qtrFbAr9-dPhPSgPJNjvBzjidMpcm-Tco9FWmrYs8ZnADBKHqdqaImhN2WGNfwveFfYH54Z1YDizvYw",
            "area_id": "5206",
            "company_id": "24484945",
            "size": 20,
            "page": 1,
            "score_type": 3,

            "sale_c2_id": "0",
            "_ENV_":
                {"source": "weixin",
                 "distribute_channel": "default",
                 "platform": "0",
                 "device_id": "a489dae0-655d-4558-9656-4fc0a42ebd9c",
                 "device_name": "",
                 "app_version": "2.6.6",
                 "os_version": "",
                 "appkey_version": "",
                 "net": "",
                 "mno": "",
                 "imei": "",
                 "open_id": 0,
                 "idfa": "",
                 "idfv": "",
                 "sn": "",
                 "mac": "",
                 "ssid": "",
                 "bssid": "",
                 "lat": 0, "lng": 0}}
        if not len(SALE_C1_IS):
            return None
        formdata['sale_c1_id'] = SALE_C1_IS.pop()
        ts = ',' + str(int(time.time()))
        sjz = ',' + str(random.randint(0, 100))
        md = hashlib.md5()
        md.update(str(formdata).encode())
        md5 = md.hexdigest().upper()
        formdata['salt_sign'] = md5 + sjz + ts
        sing_body = json.dumps(formdata)  # 4. 构建 response---engine---
        data = requests.post(url=url, data=sing_body, headers=spider.settings.get("DEFAULT_REQUEST_HEADERS"))
        redis_cli.lpush("mc","https://online.yunshanmeicai.com/mall/api/search/getsearchlistbyc2")
        return scrapy.http.TextResponse(

            url=request.url,
            status=200,
            body=data.text,
            request=request,
            encoding='utf-8'
        )

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
