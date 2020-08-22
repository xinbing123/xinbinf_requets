# *-* coding:utf8 *-*
import requests
import json
from lxml import etree
import urllib3
urllib3.disable_warnings()
headers = {

'User-Agent':'AiMeiTuan /vivo-8.1.0-vivo X20-2034x1080-480-9.12.206-900120206-867474035451169-bbk'
}

class Meituan(object):
    def __init__(self):
        self.url = 'https://chs.meituan.com/meishi/'
        self.page = 1

    def run(self):
        resp = requests.get(self.url,headers=headers,verify=False)
        text = resp.text
        print(text)
        html = etree.HTML(text)
        print(html)
if __name__ == '__main__':
    Meituan().run()
