# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import os


class MyspiderPipeline:
    def process_item(self, item, spider):
        if spider.name == 'douban':
            douban_result_file_src = os.path.abspath('.') + '/myspider/results/douban.txt'
            f = open(douban_result_file_src, "a+")
            f.write("文章名：" + item['article_name'] + "\n" + "文章链接：" + item['article_href'] + "\n" + "发帖人昵称：" + item[
                'user_name'] + "\n" + "发表人主页地址：" + item['user_href'] + "\n" + "最新回应时间：" + item[
                        'last_reply_time'] + "\n" + "评论条数：" + item['comment_count'] + "\n\n\n")
            f.close()
