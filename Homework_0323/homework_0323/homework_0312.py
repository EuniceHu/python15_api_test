# encoding: utf-8 
"""
@author: 凹凸曼
@number: 1526
@file: homework_0312.py
@time: 2019/3/13 18:38
"""
import requests,json                                        #调用requests第三库
# class UserLogin:
#     def __init__(self, login_url, param,http_method):          #初始化属性
#         self.login_url=login_url
#         self.param=param
#         self.http_method=http_method
#     @classmethod                                            #类方法
#     def HttpRequest(cls):
#         if http_method=='get':                              #判断http协议请求方法
#             resp=requests.get(login_url,param)#发送一个get请求并返回响应结果的消息实体，包含：响应报文、响应头、状态码
#         elif http_method=='post':
#             resp=requests.post(login_url,param)           #发送一个post请求返回响应结果消息的实体。
#         else:
#             print("你输入的有误，请重新输入！！！")   #这边有个小问题如果输入错误，后面的打印消息就会报错，不知道怎么调
#         return resp.json()
# if __name__=='__main__':
#     login_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
#     param = {'mobilephone': '18688773467', 'pwd': '123456'}
#     # http_method=input('请输入http请求方法get或post：')
#     http_method='post'
#     t = UserLogin(login_url,param,http_method)
#     print('响应报文:{}'.format(t.HttpRequest().text))           #响应报文
#     print('响应头:{}'.format(t.HttpRequest().headers))          #响应头
#     print('状态码:{}'.format(t.HttpRequest().status_code))      #状态码
#     print('编码格式:{}'.format(t.HttpRequest().encoding))       #获取编码格式
#     print(json.loads(t.HttpRequest().text)[ 'msg'])            #json格式的转换


class UserLogin:
    def __init__(self, login_url, param,http_method):          #初始化属性
        self.login_url=login_url
        self.param=param
        self.http_method=http_method

    def HttpRequest(self):
        if self.http_method.lower()=='get':                              #判断http协议请求方法
            try:
                resp=requests.get(self.login_url,self.param)#发送一个get请求并返回响应结果的消息实体，包含：响应报文、响应头、状态码
            except Exception as y:
                print("get请求出错")
        elif self.http_method.lower()=='post':
            resp=requests.post(self.login_url,self.param)           #发送一个post请求返回响应结果消息的实体。
        else:
            print("你输入的有误，请重新输入！！！")   #这边有个小问题如果输入错误，后面的打印消息就会报错，不知道怎么调
        return resp.json()