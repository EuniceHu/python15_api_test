# -*- coding: utf-8 -*-
# @Time    : 2019/3/13/013 17:12
# @Author  : bing
# @File    : homework_0318.py
# @Software: PyCharm


# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
import requests
class Interface_Request:

    def __init__(self,mobilephone,pwd):
        '''login参数初始化'''
        self.url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        self.dict = {'mobilephone':mobilephone,'pwd':pwd}

    def http_request(self,way):
        '''login接口请求'''
        if way=='get':
            return requests.get(self.url,self.dict).text
        elif way=='post':
            return requests.post(self.url,self.dict).text

if __name__ == '__main__':
    login = Interface_Request('18688773467','123456')
    print('get传参:',login.http_request('get'))
    print('post传参:',login.http_request('post'))


