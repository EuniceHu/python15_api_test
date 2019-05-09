#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Homework_requests_suite_ddt.py
  @time: 2019/03/25
  
  """
import unittest
import HTMLTestRunnerNew
suite=unittest.TestSuite()

from week_6.class_0321_readme import Homework_requests_testcase_ddt
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(Homework_requests_testcase_ddt))

with open('HttpRequests_ddt.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='Http_Requests的测试报告',
        description='这是关于Get和Post的测试报告',
        tester='小胡'
    )
    runner.run(suite)
