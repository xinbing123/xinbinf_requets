import json
import time
import requests
import zlib
import base64

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "Accept": "application/json",
    'Referer': 'https://chs.meituan.com/meishi/'
}

city = {
    'sz': '深圳',
    'chs': '长沙'
}
class MeituanSpider(object):

    def __init__(self):
        self.url = 'https://chs.meituan.com/meishi/pn{}/'
        self.current_page = 2
        self.session = self.init_session()

    def __http_get(self, url, params):

        resp = self.session.get(url, params=params, headers=headers)
        return resp

    def init_session(self):
        session = requests.session()
        session.get(self.url.format(self.current_page), headers=headers)
        return session

    def run(self):
        content = self.get_content()
        print(content)

    def get_content(self, city_code='sz'):
        url = "https://{}.meituan.com/meishi/api/poi/getPoiList".format(city_code)
        params = {
            'cityName': city[city_code],
            'cateId': '0',
            'areaId': '0',
            'sort': '',
            'dinnerCountAttrId': '',
            'page': self.current_page,
            'userId': '',
            'uuid': self.get_uuid(),
            'platform': 1,
            'partner': 126,
            'originUrl': self.url.format(self.current_page),
            'riskLevel': 1,
            'optimusCode': 10,
            '_token': self.get_token(city[city_code])
        }

        resp = self.__http_get(url, params)
        data = json.loads(resp.text)

        return data["data"]["poiInfos"]

    def get_uuid(self):
        return self.session.cookies['uuid']

    def get_sign(self, city_name):
        sign_dict = {
            'areaId': 0,
            'cateId': 0,
            'cityName': city_name,
            'dinnerCountAttrId': '',
            'optimusCode': 10,
            'originUrl': "https://chs.meituan.com/meishi/pn{}&page=1&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid={}".format(self.current_page,self.get_uuid()),

        }
        sign = str()
        for key, value in sign_dict.items():
            sign += (key + '=' + str(value))
        sign = base64.b64encode(zlib.compress(sign.encode())).decode()
        return sign

    def get_token(self, city_name):
        meta_token = {
            'rId': 100900,
            'ver': "1.0.6",
            'ts': int(time.time() * 1000),
            'cts': int(time.time() * 1000) + 150,
            'brVD': [1920, 1080],
            'brR': [[1920, 1080], [1920, 1040], 24, 24],
            'bI': [self.url, ""],
            'mT': [],
            'kT': [],
            'aT': [],
            'tT': [],
            'aM': '',
            'sign': self.get_sign(city_name)
        }

        token = json.dumps(meta_token)
        token = base64.b64encode(zlib.compress(str(token).encode()))

        return token.decode()


if __name__ == '__main__':

    MeituanSpider().run()


#  sign = ''"areaId=0&cateId=0&cityName=\xe9\x95\xbf\xe6\xb2\x99&dinnerCountAttrId=&optimusCode=1&originUrl=https://chs.meituan.com/meishi/pn1/&page=1&partner=126&platform=1&riskLevel=1&sort=&userId=&uuid=d80c2a67-3dcb-4c02-9d3c-d6c108983574"''