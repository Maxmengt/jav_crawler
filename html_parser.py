# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import re

class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # http://watchjavonline.com/page/\d/
        links = soup.find_all('a', class_='larger page')
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        links = soup.find_all('a', class_='page larger')
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # <a href="http://watchjavonline.com/bkd-135-mother-and-son-fucking-the-road-to-takaoka/" rel="bookmark"
        # title="Permanent Link to BKD-135 Mother And Son Fucking – The Road To Takaoka">BKD-135 Mother And Son Fucking – The Road To Takaoka</a>
        url_nodes = soup.find_all('a', rel="bookmark")
        res_data['url'] = {}
        for url in url_nodes:
            print url.string
            res_data['url'][url['href']] = url['title']

        # <img src="http://pics.dmm.co.jp/mono/movie/adult/bkd141so/bkd141sopl.jpg" alt="BKD-141 Mother And Son Fucking - Ishimori Edition" class="aligncenter size-full">
        # alt="BKD-141 Mother And Son Fucking - Ishimori Edition"
        img_nodes = soup.find_all('img', src=re.compile(r"^http://pics\.dmm\.co\.jp/mono/movie/"))
        res_data['img'] = {}

        for img in img_nodes:
            res_data['img'][img['src']] = img['alt']


        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return None, None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data