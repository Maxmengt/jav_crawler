from jav_crawler import url_manager, html_downloader, html_parser, html_outputer
import time

class CrawlerMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        Error_ = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            # time.sleep(3)
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d: %s.' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                # self.outputer.collect_data(new_data)
                self.outputer.collect_and_output_data(new_data)

                if count == 500 or Error_ == 100:
                    break
                count += 1
            except:
                Error_ += 1
                print 'craw failed.'
                continue

        # self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://watchjavonline.com/page/1/'
    obj_crawler = CrawlerMain()
    obj_crawler.craw(root_url)
