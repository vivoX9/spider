# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 百度贴吧Item
class BaiDuTiebaItem(scrapy.Item):
    article_title = scrapy.Field()
    article_link = scrapy.Field()
    author_name = scrapy.Field()
    update_time = scrapy.Field()
    article_content = scrapy.Field()

