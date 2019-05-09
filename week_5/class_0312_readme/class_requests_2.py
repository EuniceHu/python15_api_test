#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: class_requests_2.py
  @time: 2019/03/13
  
  """
import requests

# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
# login_url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# param={'mobilephone':'18688773467','pwd':'123456'}

#发送一个get请求:如果请求有参数的话 就要以字典的形式传递过去
# resp=requests.get(login_url,params=param)#响应结果消息实体  包含：响应头 响应报文 状态码
# print('响应报文:',resp.text)#响应报文
# print('响应头:',resp.headers)#响应头
# print('状态码:',resp.status_code)#状态码


# # 发送一个post请求
# resp=requests.post(login_url,data=param)#响应结果消息实体  包含：响应头 响应报文 状态码
# print('响应报文:',resp.text)#响应报文
# print('响应头:',resp.headers)#响应头
# print('状态码:',resp.status_code)#状态码


#作业安排：
#写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
#每个请求要求有请求参数
#登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
#mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码


d1={"mobilephone":'18688773467','pwd':'123456','data':None}#None

d2='{"mobilephone":"18688773467","pwd":"123456","data":null}'#null

import json

print(json.loads(d2))#字符串类型的json格式----Python的字典格式
# json格式也是键值对的形式显示，但是里面得用双引号，数据为空必须得是null




