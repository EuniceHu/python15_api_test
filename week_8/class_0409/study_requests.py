#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: study_requests.py
  @time: 2019/04/09
  
  """
import requests

"""
1:构造请求：请求方式，请求地址，请求参数
2：发起请求
3：返回响应
4：判断响应码，响应体

"""
# 注册接口
params={"mobilephone":"13037680169","pwd":"123456"}
resp=requests.get('http://test.lemonban.com/futureloan/mvc/api/member/register',
             params=params)#resp是Response的对象
print("响应码:", resp.status_code)
print("响应文本:", resp.text)
print("响应头:", resp.headers)
print("响应cookies:", resp.cookies)
print(resp.request._cookies)#request实例化对象，发送到服务端，服务端就赋值到响应的属性里面
print("cookies:", resp.request._cookies)

#登录接口


params={"mobilephone":"13037680161","pwd":"123456"}
resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',
             data=params)#resp是Response的对象 post使用data传参
print("响应码:", resp.status_code)
print("响应文本:", resp.text)
print("响应cookies：",resp.cookies)
print("请求cookies",resp.request._cookies)
print("请求方法:",resp.request.method)



#充值接口

# params={"mobilephone":"13037680161","amount":"1000"}
# resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',
#              data=params,cookies=resp.cookies)#resp是Response的对象 post使用data传参
# print("响应码:", resp.status_code)
# print("响应文本:", resp.text)
# print("响应cookies：",resp.cookies)
# print("请求cookies",resp.request._cookies)



#上一个接口的响应cookies传到下一个接口的请求cookies



#取现接口
params={"mobilephone":"13037680161","amount":"1000"}
resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/withdraw',
             data=params,cookies=resp.cookies)#resp是Response的对象 post使用data传参
print("响应码:", resp.status_code)
print("响应文本:", resp.text)
print("响应cookies：",resp.cookies)
print("请求cookies",resp.request._cookies)

