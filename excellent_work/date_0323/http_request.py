#coding:utf-8
#@time : 2019/3/21 21:46
# @Author : apple
#@file : http_request.py

import requests

class HttpRequest:
    def http_request(self,url,method,param):

        if method.lower() == 'get':
            try:#重要代码加异常处理
                resp = requests.get(url,param)#get请求
                print("get响应报文：", resp.json())
            except Exception as e:
                print("get请求出错：出错信息{}".format(e))
        else:
            try:
                resp = requests.post(url,param)#post请求
                print("post响应报文：",resp.json())
            except Exception as e:
                print("post请求出错：出错信息{}".format(e))
        return resp.json()
if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    param={'mobilephone':'18688773467','pwd':'123456'}
    re_1 = HttpRequest()
    # print('响应报文为:',HttpRequest().http_request(url,'get',param))
    print('响应报文为:', HttpRequest().http_request('http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'get', "{'mobilephone':'18688773467','pwd':'123456'}"))
