# coding utf-8
# 百度贴吧王者荣耀吧spider
# 数据格式{
#   title-帖子标题
#   href-帖子详情链接
#   author-发帖人昵称
#   time-创建时间
# }

import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu_tieba'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%CD%F5%D5%DF%C8%D9%D2%AB&fr=ala0&tpl=5']
    host = 'https://tieba.baidu.com/'

    def parse(self, response):
        res = response.xpath("//body")
        a_list = res.xpath(".//ul[@id='thread_list']//li")
        for i in a_list:
            title = i.xpath(".//a[@class='j_th_tit ']/@title").extract_first()
            href = i.xpath(".//a[@class='j_th_tit ']/@href").extract_first()
            author = i.xpath(".//span[@class='tb_icon_author ']/@title").extract_first()
            time = i.xpath(".//span[@class='threadlist_reply_date pull_right j_reply_data']/text()").extract_first()
            if title != None and href != None and author != None and time != None:
                href = self.host + href
                item = {
                    "title": title,
                    "href": href,
                    "author": author,
                    "time": time,
                }
                yield item

        next_page = res.xpath(".//div[@id='frs_list_pager']//a[@class='next pagination-item ']/@href").extract_first()

        if int(next_page.split("pn=")[1]) < 200:
            yield scrapy.Request(
                "https:" + next_page,
                callback=self.parse,
            )
