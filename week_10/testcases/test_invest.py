#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: test_invest.py
  @time: 2019/04/27
  
  """
import unittest
from week_10.common.Task_http_request import HttpRequest2
from week_10.common import Auto_do_excel
from week_10.common import do_mysql
from week_10.common import contants
from week_10.common import context
from week_10.common.context import Context
from ddt import ddt,data
# from unittest import mock

@ddt
class InvestTest(unittest.TestCase):
    excel=Auto_do_excel.DoExcel(contants.case_file,'invest')
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HttpRequest2()
    @data(*cases)
    def test_invest(self,case):
        print("开始执行测试：",case.title)
        #在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp=self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,'pass')
            #判断加标成功之后，查询数据库，取到loan_id
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'fail')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()




