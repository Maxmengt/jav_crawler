# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_and_output_data(self, data):
        if data is None or len(data) == 0:
            return
        #print data['url'][-2]

        try:
            # print data['url']
            # num = filter(str.isdigit, data['url'])
            # num = re.findall(r"\d+", data['url'])
            # print num
            # fout = open(r'E:/Acdream/Python/crawler/jav_crawler/jav_img__/' + num[0] + '.html', 'w')
            # fout.write(data['url'])
            # fout.close()
            # print data
            rstr = r"[\/\\\:\*\?\"\<\>\|\–]"  # '/\:*?"<>|'
            for href in data['url']:
                # print href
                # print '1 ' + data['url'][href]
                # print '2 ' + re.sub(rstr, "", str(data['url'][href]))
                name = re.sub(rstr, "", str(data['url'][href]))
                if name == "":
                    nae = str(data['url'][href])
                f = open(r'E:/Acdream/Python/Crawler/jav_crawler/jav_img___/' + name + '.html', 'wb')
                f.write(href)
                f.close()

            for src in data['img']:
                # print '1' , src
                u = urllib.urlopen(src)
                # print '2' + u
                data_ = u.read()
                # print '3' , data_
                # print '4' , data['img'][src]
                # print '5' , re.sub(rstr, "", str(data['img'][src]))
                name = re.sub(rstr, "", str(data['img'][src]))
                if name == "":
                    name = str(data['img'][src])
                f = open(r'E:/Acdream/Python/Crawler/jav_crawler/jav_img___/' + name + '.jpg', 'wb')
                # f = open(r'E:/Acdream/Python/Crawler/jav_crawler/jav_img___/' + data['img'][src] + '.jpg', 'wb')
                f.write(data_)
                f.close()
        except Exception:
            print Exception.message()
            print 'Error.'
            # print href
            # print data['url'][href]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        if self.datas == None or len(self.datas) == 0:
            return
        for image in self.datas:
            try:
                # num = filter(str.isdigit, data['url'])
                num = re.findall(r"\d+", data['url'])
                fout = open(r'E:/Acdream/Python/Crawler/jav_crawler/jav_img__/' + num[0] + '.html', 'w')
                fout.write(image['url'])
                fout.close()
                #print image
                rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
                for src in image['img']:
                    u = urllib2.urlopen(src)
                    data = u.read()
                    f = open(r'E:/Acdream/Python/Crawler/jav_crawler/jav_img__/' + num[0] + '_' + re.sub(rstr, "", str(image['img'][src])) + '.jpg', 'wb')
                    f.write(data)
                    f.close()
            except:
                continue

