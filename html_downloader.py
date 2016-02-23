import urllib2
import socket

class HtmlDownloader(object):

    def try_again(self, req, retries=3):
        try:
            response = urllib2.urlopen(req)
            if response.getcode() != 200:
                return None
            data = response.read()
        except Exception, what:
            print what, req
            if retries > 0:
                return self.try_again(req, retries - 1)
            else:
                print 'Get Failed:', req
                return None
        return data

    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        headers = {'User-Agent': user_agent}
        # socket.setdefaulttimeout(10)
        request = urllib2.Request(url, headers=headers)

        return self.try_again(request)
        # response = urllib2.urlopen(request)
        #
        # if response.getcode() != 200:
        #     return None
        #
        # return response.read()