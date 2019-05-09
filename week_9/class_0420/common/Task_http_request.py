#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Task_http_request.py
  @time: 2019/04/14
  
  """
import requests
from week_9.class_0416.common.config import config
class HttpRequest:
    """
    使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """
    def request(self,method,url,data=None,json=None,cookies=None):
        method=method.upper()#将method强制转换成大写
        if type(data)==str:
            data=eval(data)
#拼接请求的URL
        url=config.get('api','pre_url')+url

        if method=='GET':
            resp=requests.get(url,params=data,cookies=cookies)
        elif method=='POST':
            if json is not None:
                resp=requests.post(url,json=json,cookies=cookies)
            else:
                resp=requests.post(url,data=data,cookies=cookies)

        else:
            print('UN-support method')

        return resp

class HttpRequest2:
    """
    使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """
    def __init__(self):
        #打开一个session
      self.session=requests.sessions.session()
    def request(self,method,url,data=None,json=None):
        method = method.upper()
        if type(data) == str:
            data = eval(data)

            # 拼接请求的URL
        url = config.get('api', 'pre_url') + url
        if method == 'GET':
            resp=self.session.request(method=method,url=url,params=data)
        elif method == 'POST':
            if json:
                resp=self.session.request(method=method,url=url,json=json)
            else:
                resp=self.session.request(method=method,url=url,data=data)
        else:
            resp=None
            print('UN-support method')
        return resp

    def close(self):
        self.session.close()#用完记得关闭






if __name__ == '__main__':
    # params= {"mobilephone": "13037680161", "pwd": "123456"}
    # http_request=HttpRequest()
    # #调用登陆
    # resp1=http_request.request('POST',
    #                      'http://test.lemonban.com/futureloan/mvc/api/member/login',
    #                      data=params
    #                      )
    # print(resp1.status_code)
    # print(resp1.text)
    # print(resp1.cookies)
    # #调用充值
    # params = {"mobilephone": "13037680161", "amount": "1000"}
    # resp2=http_request.request('POST',
    #                      'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
    #                      data=params,
    #                      cookies=resp1.cookies
    #                      )
    # print(resp2.status_code)
    # print(resp2.text)
    # print(resp2.cookies)

    http_request2 = HttpRequest2()
    # 调用登陆
    params = {"mobilephone": "13037680161", "pwd": "123456"}
    resp=http_request2.request('POST',
                         'http://test.lemonban.com/futureloan/mvc/api/member/login',
                         data=params)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)
    # 调用充值
    params = {"mobilephone": "13037680161", "amount": "1000"}
    resp2=http_request2.request('POST',
                         'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                         data=params)
    http_request2.close()
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)



