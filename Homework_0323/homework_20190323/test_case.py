# -*- coding: utf-8 -*-
'''
@time: 2019/3/22 14:23
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: test_case.py
@desc:
        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +

'''

'''为我们3-12号写的http_request 请求类，写4条用例，要求利用unittest进行单元测试 ，并且用老师教的3个方法 分别去加载用例执行
4条用例里面要求有2个正常用例 2个异常用例'''

import unittest
from homework.homework_20190323.Http_Requests import HttpReq
from ddt import ddt,unpack,data #装饰器


@ddt
class TestHttp(unittest.TestCase):

    @data(*[['正确用户名，正确密码，get请求登录','http://47.107.168.87:8080/futureloan/mvc/api/member/login','get',{"mobilephone": "18688773467","pwd":"123456"},'登录成功'],
            ['正确用户名，正确密码，post请求登录', 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'post',{"mobilephone": "18688773467", "pwd": "123456"}, '登录成功'],
            ['空用户名登录', 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'get',{"mobilephone": "", "pwd": "123456"}, '手机号不能为空'],
            ['空密码登录', 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'get',{"mobilephone": "18688773467", "pwd": ""}, '密码不能为空'],
            ['错误用户名正确密码登录', 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'get',{"mobilephone": "111", "pwd": "123456"}, '用户名或密码错误'],
            ['正确用户名，错误密码登录', 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'get',{"mobilephone": "18688773467", "pwd": "111"}, '用户名或密码错误'],
            ['正确信息，错误url', 'http://47.107.168.87:8080/futureloan/mvc/api/member/login111', 'get',{"mobilephone": "18688773467", "pwd": "123456"}, '抱歉，请先登录。']
            ])
    # @data(*[{'case_title':'正确用户名，正确密码，get请求登录',
    #        'urls':'http://47.107.168.87:8080/futureloan/mvc/api/member/login',
    #        'method':'get',
    #        'params':{"mobilephone": "18688773467","pwd":"123456"},
    #        'excepted':'登录成功'}
    # ])#拆字典
    @unpack
    def test_001(self,case_title,urls,method,params,excepted,):
        print(case_title)
        # urls='http://47.107.168.87:8080/futureloan/mvc/api/member/login'  #请求地址
        # method='get'  #请求方式
        # params={'mobilephone': '18688773467','pwd':'123456'}  #请求参数
        # excepted = '登录成功'  # 期望值
        res=HttpReq().http_request(urls,method,params).json()  #返回信息
        self.assertEqual(excepted,res['msg'])  #断言登录是否成功


















