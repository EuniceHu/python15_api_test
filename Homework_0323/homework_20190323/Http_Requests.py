# -*- coding: utf-8 -*-
'''
@time: 2019/3/13 14:03
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: Http_Requests.py
@desc:
        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +

'''



'''1：作业安排： 
写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值 
每个请求要求有请求参数 
登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login 
请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码 '''
import  requests,json


class HttpReq:
    # urls = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    # payloads = {'mobilephone': '18688773467', 'pwd': '123456'}

    def http_request(self,urls,method,paramdata):
        '''完成get请求或post请求'''
        if method.lower()=='get':
            return requests.get(urls,params=paramdata)
        elif method.lower()=='post':
            return requests.post(urls,data=paramdata)


if __name__=='__main__':
    obj=HttpReq()

    urls = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    payloads = {'mobilephone': '1812312311688773467', 'pwd': '123456'}
    res=obj.http_request(urls,'get',payloads).json()
    # res=json.loads(res)
    print(res)
    print(type(res))
































