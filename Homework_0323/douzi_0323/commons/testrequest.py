# encoding=utf_8
# @Author  ： 豆子

import requests


class TestHttpRequest(object):
    def __init__(self, url, method, param, cookies=None):
        if method == 'get':
            self.req = requests.get(url=url, params=param, cookies=cookies)
        elif method == 'post':
            self.req = requests.post(url=url, data=param, cookies=cookies)
        else:
            # 其他情况暂不考虑
            pass

    def get_json_code(self):
        return self.req.json()['code']

    def get_json(self):
        return self.req.json()

    def get_cookies(self):
        return self.req.cookies

    def get_text(self):
        return self.req.text






