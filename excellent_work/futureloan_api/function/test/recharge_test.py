# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-04-15 17:48
import unittest
from ddt import ddt,data

from function.commons.base import Base
from function.commons.httpRquest import HttpRequest2
from function.commons.logger import Logger
from function.test_case.test_case import ToExcel


@ddt
class RechargeTest(unittest.TestCase):
    excel = ToExcel(Base.get_cur_dir(__file__) + '../../../data/futureloan_cases.xlsx')
    case = excel.read_excel_sheet_by_dict('recharge')

    @classmethod
    def setUpClass(cls):
        cls.request = HttpRequest2()
        cls.request.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/login',{"mobilephone":13480166986,"pwd":123456})
        cls.logger = Logger('file').getLoger()

    @data(*case)
    def test_recharge(self,case):
        print('-------测试场景：{}--------'.format(case.title))
        try:
            resp = self.request.request(case.method,case.url,case.data).json()["code"]
            try:
                self.assertEqual(resp,case.expected)
                self.excel.write_excel_rowColumn(case.case_id + 1, 7, resp, sheet='recharge')
                self.excel.write_excel_rowColumn(case.case_id + 1, 8, 'PASS', sheet='recharge')
                self.logger.info('测试场景【{}】，测试通过'.format(case.title))
            except AssertionError as a:
                self.excel.write_excel_rowColumn(case.case_id + 1, 7, resp, sheet='recharge')
                self.excel.write_excel_rowColumn(case.case_id + 1, 8, 'FAILED', sheet='recharge')
                self.logger.error('测试场景【{}】，测试不通过：{}'.format(case.title, a))
        except Exception as e:
            self.logger.error('测试场景【{}】，测试是吧-请求注册接口失败：{}'.format(case.title, e))

    @classmethod
    def tearDownClass(cls):
        cls.request.close()
        cls.excel.save()
        cls.excel.close()
