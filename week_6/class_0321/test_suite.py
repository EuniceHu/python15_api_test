# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 21:17
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_suite.py
import unittest

#存储用例的容器suite 套件

suite=unittest.TestSuite()#创建了一个对象

#第一种方法 一个一个的去添加用例
# from week_6.class_0321.learn_unittest import *
# suite.addTest(TestAdd('test_001'))#添加测试用例到suite这个套件里面  用例---测试类的实例
# suite.addTest(TestAdd('test_002'))#添加测试用例到suite这个套件里面  用例---测试类的实例
# suite.addTest(TestSub('test_002'))#添加测试用例到suite这个套件里面  用例---测试类的实例

# 第二种 通过loader来加载用例  通过模块来加载用例
from week_6.class_0321 import learn_unittest
loader=unittest.TestLoader()#用例的加载器
suite.addTest(loader.loadTestsFromModule(learn_unittest))

#第三种 通过loader来加载用例  通过测试类名来加载用例
# from week_6.class_0321.learn_unittest import *
# loader=unittest.TestLoader()#用例的加载器
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))

#执行用例
runner=unittest.TextTestRunner()#创建一个对象来执行用例
runner.run(suite)

#. 通过了一条用例
#E 代码出错
#F 用例执行失败