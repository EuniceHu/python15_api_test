# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码

import requests
from flask import json  # 引入json模块,为了将字典中的null转换为none，Python中没有null，所以为了将字符串转化为字典，需要先将null转换，否则报错

class Request:

    def http_request(self,url,d,method):
        if method.upper() == 'GET':
            res = requests.get(url,d)
        elif method.upper() == 'POST':
            res = requests.post(url,d)
        return method,res.status_code,res.headers,res.text

if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    d = {'mobilephone':'18688773467','pwd':'123456'}
    # method = 'post'
    t = Request().http_request(url,d,'get')
    print('请求方法是：{}\n状态码：{}\n响应头：{}\n响应体：{}'.format(t[0],t[1],t[2],t[3]))
    print(t)
    print(t[3])
    strdict = json.loads(t[3])#用json.loads()方法将字符串转换为字典，并且自动将字典中的null转换为none
    print(strdict)