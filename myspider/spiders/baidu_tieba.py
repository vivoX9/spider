# coding utf-8
# 百度贴吧王者荣耀吧spider
# 数据格式{
#   article_title-帖子标题
#   article_link-帖子详情链接
#   author_name-发帖人昵称
#   update_time-创建时间
#   article_content-帖子内容
# }

import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu_tieba'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%CD%F5%D5%DF%C8%D9%D2%AB&fr=ala0&tpl=5']

    def parse(self, response):
        res = response.xpath("//body")
        a_list = res.xpath(".//ul[@id='thread_list']//div[@class='col2_right j_threadlist_li_right ']")
        for i in a_list:
            item = {}

            item["article_title"] = i.xpath(
                ".//div[@class='threadlist_title pull_left j_th_tit ']//a/@title").extract_first()

            if (i.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']//a/@href").extract_first() != None):
                item["article_link"] = "https://tieba.baidu.com/" + i.xpath(
                    ".//div[@class='threadlist_title pull_left j_th_tit ']//a/@href").extract_first()

            item["author_name"] = i.xpath(".//span[@class='tb_icon_author ']/@title").extract_first()
            if item["author_name"] is not None:
                item["author_name"] = str(item["author_name"]).replace("主题作者: ", "")

            item["update_time"] = i.xpath(".//span[@class='pull-right is_show_create_time']/text()").extract_first()

            item["article_content"] = i.xpath(
                ".//div[@class='threadlist_abs threadlist_abs_onlyline ']/text()").extract_first()
            if item["article_content"] is not None:
                item["article_content"] = str(item["article_content"]).strip("\n").strip()

            if item is not None and item["article_title"] is not None and item["article_link"] is not None and item[
                "author_name"] is not None and item["update_time"] is not None and item["article_content"] is not None:
                yield item

        next_page = res.xpath(".//div[@id='frs_list_pager']//a[@class='next pagination-item ']/@href").extract_first()

        if int(next_page.split("pn=")[1]) < 200:
            yield scrapy.Request(
                "https:" + next_page,
                callback=self.parse,
            )
