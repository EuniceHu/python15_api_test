#coding:utf-8
#@time : 2019/3/24 18:08
# @Author : apple
#@file : date_0323_test_suite.py

import unittest

#存储用例的容器 suite
suite = unittest.TestSuite()#创建对象

#第二种方法：使用loader加载器，通过模块来加载用例
from homework.date_0323 import date_0323_test_case#导入模块
loader = unittest.TestLoader()#创建一个加载器对象
suite.addTest(loader.loadTestsFromModule(date_0323_test_case))

# 执行生成html测试报告--HTMLTestRunnerNew
import HTMLTestRunnerNew
with open('test.html','wb')as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file ,
        verbosity = 2,
        title= 'http_request测试报告.html',
        description= '这是一个对应http请求的测试报告',
        tester='紫梦'
    )#创建一个对象来执行用例
    runner.run(suite)