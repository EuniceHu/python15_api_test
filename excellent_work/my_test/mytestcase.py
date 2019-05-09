import unittest
import json
from TEST.requestwok import MyRequests

class MyTestCase(unittest.TestCase):

#成功用例1
    def test_case001(self):
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        data = {'mobilephone': '18688773467', 'pwd': '123456'}
        my_request = MyRequests(url, data, 'get')
        expected_code = '登录成功'
        res = json.loads(my_request.http_request().text)['msg']
        self.assertEqual(res,expected_code)

#成功用例2
    def test_case002(self):
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        data = {'mobilephone': '18688773467', 'pwd': '123456'}
        my_request = MyRequests(url, data, 'post')
        expected_code = '登录成功'
        res = json.loads(my_request.http_request().text)['msg']
        self.assertEqual(res, expected_code)

#异常用例3
    def test_case003(self):
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        data = {'mobilephone': '18688773460', 'pwd': '123456'}
        my_request = MyRequests(url, data, 'get')
        expected_code = '登录成功'
        res = json.loads(my_request.http_request().text)['msg']
        self.assertEqual(res, expected_code)

#异常用例4
    def test_case004(self):
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        data = {'mobilephone': '00', 'pwd': '00'}
        my_request = MyRequests(url, data, 'post')
        expected_code = '登录成功'
        res = json.loads(my_request.http_request().text)['msg']
        self.assertEqual(res, expected_code)