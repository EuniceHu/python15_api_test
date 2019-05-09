# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-04-19 14:34
import HTMLTestRunnerNew
import time
import unittest

from function.test.login_test import LoginTest
from function.test.recharge_test import RechargeTest
from function.test.register_test import RegisterTest

suite = unittest.TestSuite()
load = unittest.TestLoader()

suite.addTest(load.loadTestsFromTestCase(LoginTest))
suite.addTest(load.loadTestsFromTestCase(RechargeTest))
suite.addTest(load.loadTestsFromTestCase(RegisterTest))

with open('./report/futureloanTestReport{}.html'.format(time.strftime('%Y%m%d%H%M%S')),'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title='前程贷接口自动化测试报告',
                                              description='通过加载模块运行测试用例：注册、登录、充值模块接口测试',tester='胡兵')
    runner.run(suite)

