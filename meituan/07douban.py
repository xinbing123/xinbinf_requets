#
# import requests
#
# temp_url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?for_mobile=1&start=0&count=18&loc_id=108288&_=0'
#
# 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_classic_hot/items?os=ios&for_mobile=1&callback=jsonp4&start=54&count=18&loc_id=108288&_=0'
#
# headers = {'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288',
# 'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#
#
# resp = requests.get(temp_url,headers=headers)
#
#
#
# print(resp.content.decode())
#
#
import scrapy

from tutorial.items import CSDNItem
import logging


class CSDNSpider(scrapy.Spider):
    name = "csdn"

    def start_requests(self):
        start_url = 'https://mp.csdn.net/postlist/list/all/'
        cookie = {}
        headers = {
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
        }
        yield scrapy.Request(url=start_url, headers=headers, cookies=cookie)
        # yield scrapy.Request(url=start_url, headers=headers)

    def parseDetail(self, response):
        item = CSDNItem()
        item['title'] = response.css('.csdn_top::text').extract_first()
        item['body'] = response.css('#article_content .htmledit_views').extract_first()
        yield item

    def parse(self, response):

        for article in response.css('.list-item-title .article-list-item-txt'):
            articleId = article.css('a::attr("href")').extract_first()
            if articleId is not None:
                articleId = str(articleId)
                articleId = articleId[articleId.rfind("/") + 1: len(articleId)]
                next_page = 'https://blog.csdn.net/fox64194167/article/details/%s' % articleId
                yield response.follow(next_page, self.parseDetail)

        bottomNavNum = response.css('.page-item.active a::text').extract_first()
        logging.info(int(bottomNavNum))

        if bottomNavNum is not None:
            next_page = ('https://mp.csdn.net/postlist/list/all/%d' % (int(bottomNavNum) + 1))
            logging.info('next_page:' + next_page)
            yield response.follow(next_page, self.parse)





 