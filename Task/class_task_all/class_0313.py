#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_0313.py
  @time: 2019/03/13
  
  """
# 1：作业安排：
#
# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
#
# 每个请求要求有请求参数
#
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
#
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码


# Login_url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# param={'mobilephone':'18688773467','pwd':'123456'}
# import requests
# class Login:
#
#     @staticmethod
#     def http_request(login_url,params=param):
#         res=requests.get(login_url,params=param)
#         return res.text,res.headers,res.status_code
#
#
#
# if __name__ == '__main__':
#
#     t=Login()
#     t1=t.http_request(login_url='http://47.107.168.87:8080/futureloan/mvc/api/member/login')
#     print('响应报文:',t1[0])#响应报文
#     print('响应头:',t1[1])#响应头
#     print('状态码:',t1[2])#状态码



import requests
import json

class HttpRequests:
    """
    :param url:请求的网址 url
    :param params:请求的参数
    :param method:请求的方式

    """
    def __init__(self,url,params,method):
        self.url=url
        self.params=params
        self.method=method
    def httprequests(self):
        if self.method.upper()=='GET':
            res=requests.get(self.url,self.params)
        elif self.method.upper()=='POST':
            res=requests.get(self.url,self.params)
        return res

if __name__ == '__main__':
    url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    params={'mobilephone':'18688773467','pwd':'123456'}
    Login=HttpRequests(url,params,'get')
    t=Login.httprequests()
    print('响应报文:', t.text)  # 响应报文
    print('响应头:',t.headers)#响应头
    print('状态码:',t.status_code)#状态码
    # Login1=HttpRequests(url,json.loads('{"mobilephone":"18688773467","pwd":"123456"}'),'post')
    # t1=Login.httprequests()
    # print('响应报文:', t1.text)  # 响应报文
    # print('响应头:',t1.headers)#响应头
    # print('状态码:',t1.status_code)#状态码

    Login1 = HttpRequests(url, '{"mobilephone":"18688773467","pwd":"123456"}', 'post')
    t1 = Login.httprequests()
    print('响应报文:', t1.text)  # 响应报文
    print('响应头:', t1.headers)  # 响应头
    print('状态码:', t1.status_code)  # 状态码




