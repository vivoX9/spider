import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/group/593151/']

    def parse(self, response):
        print(11)
        # pass
