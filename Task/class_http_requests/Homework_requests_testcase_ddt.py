#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Homework_requests_testcase_ddt.py
  @time: 2019/03/24
  
  """


import unittest
from ddt import ddt,data,unpack
import json
from week_6.class_0321_readme.class_requests import HttpRequests

@ddt
class TestHttpGet(unittest.TestCase):
    @data(*[["登录成功",'http://47.107.168.87:8080/futureloan/mvc/api/member/login',
           {'mobilephone': '18688773467', 'pwd': '123456'}
           ]])
    @unpack
    def test_001(self,expected,url,params):
        res = HttpRequests(url, params, 'get').httprequests().text
        self.assertIn(expected, res)


    @data(*[["用户名或密码错误",'http://47.107.168.87:8080/futureloan/mvc/api/member/login',
             {'mobilephone': '19888773467', 'pwd': '123456'}
             ]])
    @unpack
    def test_002(self,expected,url,params):
        res = HttpRequests(url, params, 'get').httprequests().text
        self.assertIn(expected, res)

@ddt
class TestHttpPost(unittest.TestCase):
    @data(*[["手机号不能为空",
             'http://47.107.168.87:8080/futureloan/mvc/api/member/login',
             '{"mobilephone":"","pwd":"123456"}'
             ]])
    @unpack
    def test_001(self,expected,url,params):
        res = HttpRequests(url, params, 'post').httprequests().text
        self.assertIn(expected, res)


    @data(*[["密码不能为空",
             'http://47.107.168.87:8080/futureloan/mvc/api/member/login',
             json.loads('{"mobilephone":"18688773467","pwd":""}')
             ]])
    @unpack
    def test_002(self,expected,url,params):
        # print('http_requests_post_two')
        # expected = "密码不能为空"
        # url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        res = HttpRequests(url, params, 'post').httprequests().text
        self.assertIn(expected, res)





















