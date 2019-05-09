#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Homework_requests_testcase.py
  @time: 2019/03/22
  
  """

#总结 调用测试类的时候，一定要先创建对象之后，才能调用
"""
第一步：先导入 import  unittest  导入要测试的方法类
第二步：编写测试用例类，一定要继承unittest.TestCase类
第三步：编写测试用例，一定要用test开头，不然执行不出来
第四步：在测试用例里面，编写期望值，实际值，实际值是导入的方法类，
一定要在类名后面加()创建对象，传参数，之后用assert断言
第五步：新建模块，使用suite存储用例，先导入import unittest
第六步：创建个TestSuite类的对象TestSuite(),创建对象，才能调用方法
第七步：有三种方法来加载用例
1：一个一个加，导入所有测试类，用TestSuite()调用addTest()方法
2：使用Loader来加载，导入模块，创建个TestLoader类的对象TestLoader(),来调用LoadTestsFromModule方法
3：使用Loader来加载，导入所有测试类，创建个TestLoader类的对象TestLoader(),来调用loadTestsFromTestCase方法
第八步：执行用例，首先要创建个TextTestRunner类的对象TextTestRunner()
用TextTestRunner()调用run方法使用Suite
TextTestRunner().run(Suite)

"""
import unittest
import json
from week_6.class_0321_readme.class_requests import HttpRequests


class TestHttpGet(unittest.TestCase):
    def test_001(self):
        print('http_requests_get_one')
        expected="登录成功"
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        params = {'mobilephone': '18688773467', 'pwd': '123456'}
        res=HttpRequests(url,params,'get').httprequests().text
        self.assertIn(expected,res)
    def test_002(self):
        print('http_requests_get_two')
        expected="用户名或密码错误"
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        params = {'mobilephone': '18688773467', 'pwd': '12345678'}
        res=HttpRequests(url,params,'get').httprequests().text
        self.assertIn(expected,res)
class TestHttpPost(unittest.TestCase):
    def test_001(self):
        print('http_requests_post_one')
        expected="手机号不能为空"
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        res=HttpRequests(url, '{"mobilephone":"","pwd":"123456"}', 'post').httprequests().text
        self.assertIn(expected,res)
    def test_002(self):
        print('http_requests_post_two')
        expected="登录成功"
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        res=HttpRequests(url,json.loads('{"mobilephone":"18688773467","pwd":"123456"}'),'post').httprequests().text
        self.assertIn(expected,res)
