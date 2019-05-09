import unittest
from class_homework.unittest import test_unit
import HTMLTestRunnerNew

suite=unittest.TestSuite()

loader=unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(test_unit.Test_Case))

with open('report.html',mode='wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='unittest',description='接口请求',tester='空白')
    runner.run(suite)