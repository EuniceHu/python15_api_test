

#!/usr/bin/python3

# Author:xuqiao

# Time:2019/3/2318:22

# File:unittest_suite_httpcase.

# Email:1462942304@qq.

import unittest

import HTMLTestRunner

import test_login

class TestHttpSuite:

    def http_suite_runner_001(self):

        """采用loader来加载用例,通过模块名来加载"""

        # suite 收集期，容器，用来收集我们的测试用例
        suite=unittest.TestSuite()

        loader=unittest.TestLoader()

        suite.addTest(loader.loadTestsFromModule(test_login))
        # 上下文管理器 ==》 一定阶段会执行特定操作。

        with open("http_report.html","wb") as file:

            runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="测试http请求的测试报告", description="一共写了4条测试用例")

            runner.run(suite)

    def http_suite_runner_002(self):

        """用loader来加载用例，通过类名来加载"""

        suite=unittest.TestSuite()

        loader=unittest.TestLoader()

        suite.addTest(loader.loadTestsFromTestCase(test_login.HttpTestCase))

        with open("http_report.html","wb")as file:

            runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="测试http请求的测试报告", description="一共写了4条测试用例")

            runner.run(suite)




if __name__ == '__main__':

    TestHttpSuite().http_suite_runner_001()



