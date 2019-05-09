# encoding=utf_8
# @Author  ： 豆子

import unittest
from HTMLTestRunner import HTMLTestRunner

from douzi_0323.commons import filepath

discover = unittest.defaultTestLoader.discover(filepath.case_dir, 'test*.py')

with open(filepath.report_dir, 'wb+') as file:
    runner = HTMLTestRunner(stream=file, title='测试报告', description='api测试')
    runner.run(discover)
