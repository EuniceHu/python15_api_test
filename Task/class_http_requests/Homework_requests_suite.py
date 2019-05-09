#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Homework_requests_suite.py
  @time: 2019/03/22
  
  """
import unittest
import HTMLTestRunnerNew

#先创建TestSuite类的对象TestSuite()
suite=unittest.TestSuite()

#第一种方法 一个一个的去添加用例
# from week_6.class_0321_readme.Homework_requests_testcase import *
# suite.addTest(TestHttpGet("test_001"))
# suite.addTest(TestHttpGet("test_002"))
# suite.addTest(TestHttpPost("test_001"))
# suite.addTest(TestHttpPost("test_001"))

#第二种方法 通过Loader来加载用例  通过模块名来加载用例
# from week_6.class_0321_readme import Homework_requests_testcase
# loader=unittest.TestLoader()#创建TestLoader的对象TestLoader()
# suite.addTest(loader.loadTestsFromModule(Homework_requests_testcase))

#第三种 通过loader来加载用例  通过测试类名来加载用例
from week_6.class_0321_readme.Homework_requests_testcase import *
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpGet))
suite.addTest(loader.loadTestsFromTestCase(TestHttpPost))


#执行用例

# runner=unittest.TextTestRunner()#创建一个对象来执行用例
# runner.run(suite)

with open('Http_Requests.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='Http_Requests的测试报告',
        description='这是关于Get和Post的测试报告',
        tester='小胡'
    )
    runner.run(suite)