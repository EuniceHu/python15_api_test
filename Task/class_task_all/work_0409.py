# 1，扩展之前实现好的http_request，支持传cookies
# 2，完成接口文档中注册，登录，充值的调用
# 3，熟悉之前发给你们的接口文档和需求介绍视频，做个每个接口功能了然于心！！！

import requests

class Request:

    def http_request(self,url,d,method,request_cookies=None):
        if method.upper() == 'GET':
            res = requests.get(url,d,cookies=request_cookies)
        elif method.upper() == 'POST':
            res = requests.post(url,d,cookies=request_cookies)
        return method,res.status_code,res.headers,res.json(),res.cookies,res.request._cookies

register_resp = Request().http_request('http://test.lemonban.com/futureloan/mvc/api/member/register',
                                  {'mobilephone': '13125256363', 'pwd': '123456'}, 'post')

print('请求方法是：{}\n状态码：{}\n响应头：{}\n响应体：{}\n响应Cookies：{}\n请求Cookies：{}'.format(register_resp[0],
       register_resp[1], register_resp[2],register_resp[3],register_resp[4],register_resp[5]))

login_resp = Request().http_request('http://test.lemonban.com/futureloan/mvc/api/member/login',
                                     {'mobilephone': '13125256363', 'pwd': '123456'},'post')

print('请求方法是：{}\n状态码：{}\n响应头：{}\n响应体：{}\n响应Cookies：{}\n请求Cookies：{}'.format(login_resp[0],
       login_resp[1],login_resp[2],login_resp[3],login_resp[4],login_resp[5]))

recharge_resp = Request().http_request('http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                            {'mobilephone': '13125256363', 'amount': '10'},'post',request_cookies=login_resp[4])

print('请求方法是：{}\n状态码：{}\n响应头：{}\n响应体：{}\n响应Cookies：{}\n请求Cookies：{}'.format(recharge_resp[0],
       recharge_resp[1], recharge_resp[2],recharge_resp[3], recharge_resp[4],recharge_resp[5]))
