# -*- coding: utf-8 -*-

# Scrapy settings for meichai project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meichai'

SPIDER_MODULES = ['meichai.spiders']
NEWSPIDER_MODULE = 'meichai.spiders'
#指定了去重的类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#制定了调度器的类
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#调度器的内容是否持久化
SCHEDULER_PERSIST = True

#redis的url地址
REDIS_URL = "redis://127.0.0.1:6379"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
DEFAULT_REQUEST_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://passport.yunshanmeicai.com",
    "Referer": "https://passport.yunshanmeicai.com/pc/site/index",
    "Cookies":"is_wx_new=1; mc_loguser_source=weixin; mc_loguser_channel=default; meicai_used=1; weixin_ticket=yPLlIYupjqi4JlxW2kahqLdvYTF0tqrGe8dHJhnDZG4EzA1xBIf%2BOD9XtDojr5eyXOmx0AZ6RET3iyQmzZQqx5ZN1OO4DT9RQ2b1d%2FVIZBxcFy4SstHY9B6kcmCPMx6jueFfyVPIayUoPaGrwXQuD2B%2F5njDb0KHe4OK%2FZxLya7QKxtrYWtTKwuFPZSBKmALWho4HPVymwtn7TmwghGcMg6oZMgpIshd8EkcM%2FH5%2BIpuC5kzMsvYiNBVAywVm1GOuB2QTFXoYVWc8KjLcsi%2FxJs6YU25m0tg20FSATKLkEeM%2F%2FpljfGnZo6%2BIdArKsNlUlJAAD3JdA1AajMc9HibzgRoPC1xkTqbQOqcYdJvNBBRxO2yXmE7G2zGlyhA6ZXn4EGu468iB3iKjnsuRx3NmQ%3D%3D; mc_loguser_tickets=jwt%3AeyJhbGciOiJSUzI1NiJ9.eyJpZCI6IjIwMzg5OTc5IiwianRpIjoiOTYyYmYwNjc5NDY4MTEzOWI5NDk5Y2I2NGNmZGNkNDMiLCJpYXQiOjE1NTk1Njg2MDY2MzJ9.t0csg4r-X_AVcxP0zg_uzACRtAkau10a87fHE8-O8E4fGqdC5e3QVbYFin_zFN70C_t3byxmU7PXpI6Ep5FcewAYV0R6qtrFbAr9-dPhPSgPJNjvBzjidMpcm-Tco9FWmrYs8ZnADBKHqdqaImhN2WGNfwveFfYH54Z1YDizvYw; meicai_gray_flag=7_5206_24484945; mc_loguser_company=24484945; mc_loguser_passport=20389979; pay_weixin_ticket=yPLlIYupjqi4JlxW2kahqLdvYTF0tqrGe8dHJhnDZG4EzA1xBIf%2BOD9XtDojr5eyXOmx0AZ6RET3iyQmzZQqx5ZN1OO4DT9RQ2b1d%2FVIZBxcFy4SstHY9B6kcmCPMx6jueFfyVPIayUoPaGrwXQuD2B%2F5njDb0KHe4OK%2FZxLya7QKxtrYWtTKwuFPZSBKmALWho4HPVymwtn7TmwghGcMg6oZMgpIshd8EkcM%2FH5%2BIpuC5kzMsvYiNBVAywVm1GOuB2QTFXoYVWc8KjLcsi%2FxJs6YU25m0tg20FSATKLkEeM%2F%2FpljfGnZo6%2BIdArKsNlUlJAAD3JdA1AajMc9HibzgRoPC1xkTqbQOqcYdJvNBBRxO2yXmE7G2zGlyhA6ZXn4EGu468iB3iKjnsuRx3NmQ%3D%3D; mc_loguser_city=7; mc_loguser_area=5206"
}

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3  爬虫延迟
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16  配置每个ip请求并发

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
LOG_LEVEL = "WARNING"

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'meichai.middlewares.MeichaiSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'meichai.middlewares.MeichaiDownloaderMiddleware': 543,
}

# Enable or disable extensions
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'meichai.pipelines.MeichaiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
