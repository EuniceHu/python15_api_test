# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/3/22 10:43

import requests
from lesson_0321.http_request_0312 import *
import unittest
# import json
from ddt import ddt,data,unpack

@ddt
class TestHttpRequest(unittest.TestCase):
    '''
    定义一个类，每条用例作为一个列表，其中的params参数用一个字典存储
    '''

    @data([{'mobilephone': '18688773467', 'pwd': '123456'}, '登录成功','GET'],#正常用例，请求方式为get
          [{'mobilephone': '18688773467', 'pwd': '123456'}, '登录成功', 'POST'],#正常用例，请求方式为post
          [{'mobilephone': '18688773467', 'pwd': ''}, '密码不能为空'],#异常用例：手机号正确，密码为空
          [{'mobilephone': '18688773467', 'pwd': '12345678'}, '用户名或密码错误'])#异常用例：手机号正确，密码错误
    @unpack
    def test_001(self,params,excepted,method='GET'):
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        res = HttpRequest(url, params, method='get').http_request().json()  #将响应数据转换为字典格式
        print(res) #打印实际结果，在生成的测试报告详情中可以看到
        self.assertEqual(excepted, res["msg"])

