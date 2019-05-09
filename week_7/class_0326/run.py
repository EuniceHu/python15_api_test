import unittest
import HTMLTestRunner
import test_login

def main():

    # 加载用例
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromModule(test_login))

    # 生成报告
    with open("http_report.html", "wb") as file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title="测试http请求的测试报告",
                                               description="一共写了4条测试用例")

        runner.run(suite)


if __name__ == '__main__':
    main()