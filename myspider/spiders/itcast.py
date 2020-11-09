import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['www.douban.com']  # 允许爬取的范围
    start_urls = ['https://www.douban.com/group/593151/discussion']

    def parse(self, response):
        wrapper = response.xpath("//div[@id='wrapper']")
        list = response.xpath("//table[@class='olt']//tr")
        next_page_link = wrapper.xpath("//div[@class='paginator']//span[@class='next']//a/@href").extract_first()
        for li in list:
            total_td = li.xpath(".//td")
            article_name = total_td[0].xpath(".//a/text()").extract_first()
            article_href = total_td[0].xpath(".//a/@href").extract_first()
            user_name = total_td[1].xpath(".//a/text()").extract_first()
            user_href = total_td[1].xpath(".//a/@href").extract_first()
            publish_time = total_td[3].xpath("./text()").extract_first()
            comment_count = total_td[2].xpath("./text()").extract_first()
            if article_name != None and article_href != None and user_name != None and user_href != None and publish_time != None and comment_count != None:
                data = {
                    "article_name": article_name.replace("\n", '').strip(),
                    "article_href": article_href,
                    "user_name": user_name,
                    "user_href": user_href,
                    "publish_time": publish_time,
                    "comment_count": comment_count,
                }
                yield data
        #   重复爬取直至到100条数据
        if int(next_page_link.split('start=')[1]) < 100:
            yield scrapy.Request(
                next_page_link,
                callback=self.parse,
            )
