# -*- coding: utf-8 -*-
# @Time    : 2019/3/22/022 14:23
# @Author  : bing
# @File    : test_case.py
# @Software: PyCharm

import unittest
import json
from homework_0322.request_login import Interface_Request

class Test_request_faile(unittest.TestCase):

    def test_001(self):#利用‘get’方式传参，用户名及密码正确的校验     预期："msg":"登录成功"
        print('Test_get_login')
        expected="登录成功"#期望值
        res=Interface_Request('18688773467','123456').http_request('get') #实际值
        #断言
        self.assertEqual(expected,json.loads(res)['msg'])

    def test_002(self):#利用‘post’方式传参，用户名及密码正确的校验     预期："msg":"登录成功"
        print('Test_post_login')
        expected="登录成功"#期望值
        res=Interface_Request('18688773467','123456').http_request('post') #实际值
        #断言
        self.assertIn(expected,res)


class Test_request_success(unittest.TestCase):

    def test_001(self):#利用'get'方式传参，用户名正确，密码错误    预期："msg":"用户名或密码错误"
        print('Test_get_user_or_password_faile')
        expected="用户名或密码错误"#期望值
        res=Interface_Request('18688773467','12345678').http_request('get') #实际值
        #断言
        self.assertEqual(expected,json.loads(res)['msg'])

    def test_002(self):#利用'get'方式传参，用户名为空，密码正确    预期："msg":"手机号不能为空"
        print('Test_get_user_is_null')
        expected="手机号不能为空"#期望值
        res=Interface_Request('','123456').http_request('get') #实际值
        #断言
        self.assertIn(expected, res)


