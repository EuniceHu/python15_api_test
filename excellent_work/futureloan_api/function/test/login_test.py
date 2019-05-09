# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-04-15 17:48
import unittest

from ddt import ddt, data

from function.commons.base import Base
from function.commons.httpRquest import HttpRequest
from function.commons.logger import Logger
from function.test_case.test_case import ToExcel


@ddt
class LoginTest(unittest.TestCase):
    excel = ToExcel(Base.get_cur_dir(__file__) + '../../../data/futureloan_cases.xlsx')
    case = excel.read_excel_sheet_by_dict('login')
    logger = Logger("file").getLoger()
    request = HttpRequest()

    @data(*case)
    def test_login(self, case):
        print('-------测试场景：{}--------'.format(case.title))
        try:
            resp = self.request.request(case.method, case.url, case.data).text
            try:
                self.assertEqual(resp, case.expected)
                self.excel.write_excel_rowColumn(case.case_id + 1, 7, resp, sheet='login')
                self.excel.write_excel_rowColumn(case.case_id + 1, 8, 'PASS', sheet='login')
                self.logger.info('登录测试场景【{}】测试通过'.format(case.title))
            except AssertionError as e:
                self.excel.write_excel_rowColumn(case.case_id + 1, 7, resp, sheet='login')
                self.excel.write_excel_rowColumn(case.case_id + 1, 8, 'FAILED', sheet='login')
                self.logger.warn('登录测试场景【{}】测试不通过：{}'.format(case.title, e))
        except Exception as e:
            self.logger.error("请求失败：{}".format(e))
            print("请求失败：{}".format(e))
        finally:
            self.excel.save()
            self.excel.close()
