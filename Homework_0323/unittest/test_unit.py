import unittest
from class_homework.unittest.test_request import Request
from class_homework.unittest import test_data
from class_homework.unittest.test_logger import Logger
from ddt import ddt,data



@ddt
class Test_Case(unittest.TestCase):

    def setUp(self):
        self.Request=Request()
        self.logger=Logger()

    @data(*test_data.param)
    def test_request(self,item):
        self.logger.info('正在执行第{}条用例，测试数据是：{}'.format(item['id'],item['param']))
        result=self.Request.request(item['method'],item['url'],item['param']).json()
        self.logger.info('期望结果是：{}，实际结果是{}'.format(item['expected'],result['code']))
        try:
            self.assertEqual(item['expected'],result['code'])
        except AssertionError as error:
            self.logger.error('断言错误是：{}'.format(error))
            raise error

