#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Extension_requests.py
  @time: 2019/04/10
  
  """
# 1,扩展之前实现好的http_request，支持传cookies
#
# 2，完成接口文档中注册，登录，充值的调用
#
# 3，熟悉之前发给你们的接口文档和需求介绍视频，做个每个接口功能了然于心！！！


import requests
class HttpRequests:

    def http_request(self,url,param,method,cookies=None):
        if method.lower()=='get':#判断请求方法为get还是post
            resp=requests.get(url,param,cookies=cookies)
            print('get响应报文:',resp.text)
            print('get响应cookies',resp.cookies)
            print('get请求cookies',resp.request._cookies)
        elif method.lower()=='post':
            resp=requests.post(url,data=param,cookies=cookies)
            print('post响应报文:',resp.text)
            print('post响应cookies',resp.cookies)
            print('post请求cookies',resp.request._cookies)
        return resp



if __name__ == '__main__':
    #注册接口
    reg=HttpRequests().http_request(
        url='http://test.lemonban.com/futureloan/mvc/api/member/register',
        param={"mobilephone":"13037680161","pwd":"123456"},
        method='get',
    )
    print(reg)
    #登录接口
    login=HttpRequests().http_request(
        url='http://test.lemonban.com/futureloan/mvc/api/member/login',
        param={"mobilephone":"13037680161","pwd":"123456"},
        method='post',
    )
    cookies=login.cookies
    print(cookies)

    # 充值接口
    rech=HttpRequests().http_request(
        url='http://test.lemonban.com/futureloan/mvc/api/member/recharge',
        param={"mobilephone":"13037680161","amount":"1000"},
        method='post',
        cookies=cookies
    )
    print(rech.json())




