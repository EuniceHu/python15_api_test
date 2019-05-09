#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_requests_one.py
  @time: 2019/04/02
  
  """
# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
#
# 每个请求要求有请求参数
#
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
#
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码

import requests
class UserLogin:
    '''初始化方法，参数有URL param，请求方法'''
    def __init__(self,url,param,method):
        self.url=url
        self.param=param
        self.method=method
    def http_request(self):
        if self.method.lower()=='get':#判断请求方法为get还是post
            resp=requests.get(self.url,self.param)
            print('get响应报文:',resp.text)
        elif self.method.lower()=='post':
            resp=requests.post(self.url,self.param)
            print(resp)
            print(resp.json())
            print('post响应报文:',resp.text)
        return resp.json()



if __name__ == '__main__':
    user=UserLogin(
            url='http://47.107.168.87:8080/futureloan/mvc/api/member/login',
            param={'mobilephone':'18688773467','pwd':'123456'},
            method='post'
        )
    user.http_request()



