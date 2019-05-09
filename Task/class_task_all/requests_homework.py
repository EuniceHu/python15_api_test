1  # -*- coding: utf-8 -*-#
2  #project_name  python15
3  # Name:         requests_homework
4  # Author:       微微
5  # Date:         2019/3/13
6  #-------------------------------------------------------------------------------

# 1：写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数 ,登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
import requests
import json
class Requests:
    def __init__(self,url,param,method):
        self.url=url
        self.param=param
        self.method=method
    def http_requests(self):
        if self.method.upper()=='GET':
            return (requests.get(self.url,self.param))
        elif self.method.upper()=='POST':
            return(requests.post(self.url,self.param))

if __name__=='__main__':
    res=Requests('http://47.107.168.87:8080/futureloan/mvc/api/member/login',{'mobilephone':'18688773467','pwd':'123456'},'get').http_requests()
    print(res.text)
    print(res.status_code)
    print(res.headers)
    res1=Requests('http://47.107.168.87:8080/futureloan/mvc/api/member/login',json.loads('{"mobilephone":"18688773467","pwd":"123456"}'),'post').http_requests()
    print(res1.text)
    print(res1.status_code)
    print(res1.headers)