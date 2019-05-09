#2：为我们3-12号写的http_request 请求类，写4条用例，要求利用unittest进行单元测试
# 并且用老师教的3个方法 分别去加载用例执行3：4条用例里面要求有2个正常用例 2个异常用例

import unittest
from TEST.mytestcase import MyTestCase
from TEST import mytestcase

#手动加载
my_suite=unittest.TestSuite()
# my_suite.addTest(MyTestCase('test_case001'))
# my_suite.addTest(MyTestCase('test_case002'))
# my_suite.addTest(MyTestCase('test_case003'))
# my_suite.addTest(MyTestCase('test_case004'))

#模块名加载
# my_loader=unittest.TestLoader()
# my_suite.addTest(my_loader.loadTestsFromModule(mytestcase))

#类名加载
my_loader=unittest.TestLoader()
my_suite.addTest(my_loader.loadTestsFromTestCase(MyTestCase))

runner=unittest.TextTestRunner()
runner.run(my_suite)