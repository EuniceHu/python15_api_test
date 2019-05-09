# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-04-12 23:32
import json

import requests


class HttpRequest:

    def request(self, method, url, params, types='data', cookies=None):
        method = method.upper()
        resp = None
        if method == 'GET':
            resp = requests.get(url=url, params=params, cookies=cookies)
        elif method == 'POST':
            if types == 'data':
                resp = requests.post(url, data=params, cookies=cookies)
            else:
                resp = requests.post(url, json=params, cookies=cookies)

        return resp


class HttpRequest2:

    def __init__(self):
        self.session = requests.sessions.session()

    def request(self, method, url, params, types='data'):
        method = method.upper()
        resp = None
        if method == 'GET':
            resp = self.session.request(method, url, params=params)
        elif method == 'POST':
            if types == 'data':
                resp = self.session.request(method, url, data=params)
            else:
                resp = self.session.request(method, url, json=params)

        return resp

    def close(self):
        self.session.close()


if __name__ == '__main__':
    httpRequest = HttpRequest()
    # 登录
    loginUrl = r'http://test.lemonban.com/futureloan/mvc/api/member/login'
    params = {
        "mobilephone": 13480166986,
        "pwd": 123456
    }

    resp = httpRequest.request('get', loginUrl, params)

    # 充值
    rechargeUrl = r'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    params = {
        "mobilephone": 13480166986,
        "amount": 1000
    }

    resp = httpRequest.request('post', rechargeUrl, params, cookies=resp.cookies)
    print(resp.text)
