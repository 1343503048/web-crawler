# coding:utf8
import Html_downloader
import Html_outputer
import Html_parser
import url_manager

#  爬虫框架

class ClwerMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = Html_downloader.HtmlDownloader()
        self.parser = Html_parser.HtmlParser()
        self.outputer = Html_outputer.HtmlOutputer()


    def craw(self, root_url):
        cnt = 1  # 记录当前爬取的url数
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d: %s' % (cnt, new_url)
                cnt += 1
                if cnt == 20:
                    break;
                print "download html..."
                html_cont = self.downloader.download(new_url)
                print "html download successfully..."
                print "parser html..."
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                print "html parser successfully..."
                if new_data is None:
                    continue
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

            except:
                print "failed"

        print  "saving data as html..."
        self.outputer.output_html()
        print "finished"

if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = ClwerMain()
    obj_spider.craw(root_url)