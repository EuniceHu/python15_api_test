# -*- coding: utf-8 -*-
'''
@time: 2019/3/25 14:19
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: test_suite_new.py
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
'''
1：测试数据结合ddt来使用
2：出具一份测试报告'''

import unittest
import HTMLTestRunnerNew

suite=unittest.TestSuite()  #创建测试集


from homework.homework_20190323 import test_case
loader=unittest.TestLoader()   #创建加载器
suite.addTest(loader.loadTestsFromModule(test_case))


#运行测试用例并生成html测试报告
with open('report.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='HTTP请求-测试报告',
        description=None,
        tester='Mr.Right')
    runner.run(suite)












