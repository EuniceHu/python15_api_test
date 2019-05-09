# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 21:17
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_suite.py
import unittest
import HTMLTestRunnerNew

#存储用例的容器suite 套件
suite=unittest.TestSuite()#创建了一个对象

#第一种改源码的方案--不太合适  又要改回来
# from week_6.class_0321.learn_unittest import *
# test_data=[[0,0,0],[1,1,2],[-1,-2,-3]]#a b expected---->数据可以来自于Excel
# for item in test_data:
#     suite.addTest(TestAdd(item[0],item[1],item[2],'test_001'))
#

# 第二种 通过loader来加载用例  通过模块来加载用例
# from week_6.class_0321 import learn_unittest
# loader=unittest.TestLoader()#用例的加载器
# suite.addTest(loader.loadTestsFromModule(learn_unittest))



#执行用例--unittest版本
# with open('test.txt','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
#     runner.run(suite)

#执行并生成html测试报告--HTMLTestRunnerNew
with open('test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='20190323py15测试报告',
        description='这是一个加法和减法功能验证的测试报告',
        tester='今天有点不一样的华华'
    )#创建一个对象来执行用例
    runner.run(suite)#这一行没有任何改变

# github
#. 通过了一条用例
#E 代码出错
#F 用例执行失败


#pip install ddt
