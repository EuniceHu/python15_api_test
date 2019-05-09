#1：作业安排： 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
import  requests
import json
class MyRequests:
    def __init__(self,url,data,method):
        self.url=url
        self.data=data
        self.method=method

    def http_request(self):
        if self.method=='get':
            res=requests.get(self.url,self.data)
            return res
        if self.method=='post':
            res=requests.post(self.url,self.data)
            return res

if __name__=='__main__':
    url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    data={'mobilephone':'18688773467','pwd':'123456'}
    my_request=MyRequests(url,data,'get')
    print('get响应头：',my_request.http_request().headers)
    print('get响应码：',my_request.http_request().status_code)
    print('get响应报文：',my_request.http_request().text)
    my_request=MyRequests(url,data,'post')
    print('post响应头：',my_request.http_request().headers)
    print('post响应码：',my_request.http_request().status_code)
    x=json.loads(my_request.http_request().text)
    print(type(x))
    print('post响应报文：',x['msg'])