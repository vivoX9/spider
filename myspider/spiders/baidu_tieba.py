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

    def parse(self, response):
        res = response.xpath("//body")
        a_list = res.xpath(".//ul[@id='thread_list']//div[@class='threadlist_lz clearfix']")
        for i in a_list:
            item = {}

            item["title"] = i.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']//a/@title").extract_first()

            if(i.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']//a/@href").extract_first() != None):
                item["href"] = "https://tieba.baidu.com/" + i.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']//a/@href").extract_first()

            item["author"] = i.xpath(".//span[@class='tb_icon_author ']/@title").extract_first()

            item["time"] = i.xpath(".//span[@class='pull-right is_show_create_time']/text()").extract_first()

            if(item != None and item["title"] != None and item["href"] != None and item["author"] != None and item["time"] != None):
                yield item

        next_page = res.xpath(".//div[@id='frs_list_pager']//a[@class='next pagination-item ']/@href").extract_first()

        if int(next_page.split("pn=")[1]) < 200:
            yield scrapy.Request(
                "https:"+next_page,
                callback=self.parse,
            )