import unittest

suite = unittest.TestSuite()

# 加载用例的方式一：一条一条添加用例
# from work_0321_testcase import *
# suite.addTest(TestGetRequest('test_phone_pwd_correct'))
# suite.addTest(TestGetRequest('test_pwd_wrong'))
# suite.addTest(TestPostRequest('test_phone_pwd_correct'))
# suite.addTest(TestPostRequest('test_pwd_wrong'))

# 加载用例的方式二：通过loader来加载整个模块的用例
# import work_0321_testcase
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(work_0321_testcase))

# 加载用例的方式三：通过loader来加载一个测试类的用例
# from work_0321_testcase import *
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestPostRequest))
# suite.addTest(loader.loadTestsFromTestCase(TestGetRequest))

runner =unittest.TextTestRunner()
runner.run(suite)