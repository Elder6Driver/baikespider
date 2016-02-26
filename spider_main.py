# coding:utf8

__author__ = 'AlexPC'

from baike_spider import url_manager, html_downloader, html_parser, html_output


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()

    # 这个方法是不断爬取得方法
    def craw(self, root_url):
        # 统计是第几个url
        count = 1
        # 添加单个url
        self.urls.add_new_url(root_url)
        # 只要urls中还有url
        while self.urls.has_new_url():
            try:
                # 从urls中取得一个url
                new_url = self.urls.get_new_url()
                # 打印url信息
                print 'craw %d : %s' % (count, new_url)
                # 使用downloader下载这个url中的html内容
                html_cont = self.downloader.download(new_url)
                # 使用parser解析这个url中的内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将解析到的新url放入urls中
                self.urls.add_new_urls(new_urls)
                # 将解析到的内容放入outputer中
                self.outputer.collect_data(new_data)

                if count >= 10:
                    break

                count = count + 1
            except:
                print 'failed'

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
