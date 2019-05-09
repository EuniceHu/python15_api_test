#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Task_testsuite.py
  @time: 2019/04/02
  
  """
import unittest
import HTMLTestRunnerNew

suite=unittest.TestSuite()#创建TestSuite的类

from Task.class_http_requests import Task_openpyxl_testcase#导入模块
loader=unittest.TestLoader()#创建TestLoader的对象
suite.addTest(loader.loadTestsFromModule(Task_openpyxl_testcase))


with open('Task_http.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='测试报告',
        description='这是一个新的测试报告',
        tester='小胡'
    )
    runner.run(suite)




