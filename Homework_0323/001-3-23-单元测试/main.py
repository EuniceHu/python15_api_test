import unittest
from test_request import TestRequest
import HTMLTestRunnerNew
# 当前时间
import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 文件名不支持冒号
nowTime1 = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')


print('report'+str(nowTime1)+'.html')
suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRequest))
with open('test_report'+str(nowTime1)+'.html', 'wb') as file:
    HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description=nowTime,tester='001').run(suite)