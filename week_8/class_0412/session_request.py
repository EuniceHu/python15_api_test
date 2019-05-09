#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: session_request.py
  @time: 2019/04/14
  
  """
"""
两种传递cookie的方式
1：单独的session,从上一个请求的返回cookies,指定传递到下一个请求的入参cookie当中
2：使用同一个session,就会自动传递cookie
"""
import requests
session=requests.sessions.session()
#登陆
params= {"mobilephone": "13037680161", "pwd": "123456"}
resp1=session.request('POST',
                url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                data=params)
print(resp1.status_code)
print(resp1.text)
print(resp1.cookies)
#充值
params = {"mobilephone": "13037680161", "amount": "1000"}
resp2=session.request('POST',
                'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                data=params)
print(resp2.status_code)
print(resp2.text)
print(resp2.cookies)

session.close()#把session关闭