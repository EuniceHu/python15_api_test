# -*- coding: utf-8 -*-
# @Author  : hubing   
# @mail    : cocofei-f@163.com
# @Date    : 2019-04-15 17:48
import random
import string
import unittest
from ddt import ddt, data
from function.commons.base import Base
from function.commons.httpRquest import HttpRequest2
from function.commons.logger import Logger
from function.test_case.test_case import ToExcel


@ddt
class RegisterTest(unittest.TestCase):
    excel = ToExcel(Base.get_cur_dir(__file__) + '../../../data/futureloan_cases.xlsx')
    case = excel.read_excel_sheet_by_dict('register')
    logger = Logger('file').getLoger()

    def setUp(self):
        self.http_request = HttpRequest2()

    @data(*case)
    def test_register(self, case):
        print('-------测试场景：{}--------'.format(case.title))
        try:
            if case.data['mobilephone'] == ('register_mobile'):
                case.data['mobilephone'] = RegisterTest.mobile_phone()

            resp = self.http_request.request('POST', case.url, case.data).text
            try:
                self.assertEqual(resp, case.expected)
                self.excel.write_excel_rowColumn(case.case_id + 1, 7, resp, sheet='register')
                self.excel.write_excel_rowColumn(case.case_id + 1, 8, 'PASS', sheet='register')
                self.logger.info('测试场景【{}】，测试通过'.format(case.title))
            except AssertionError as a:
                self.excel.write_excel_rowColumn(case.case_id + 1, 7, resp, sheet='register')
                self.excel.write_excel_rowColumn(case.case_id + 1, 8, 'FAILED', sheet='register')
                self.logger.error('测试场景【{}】，测试不通过：{}'.format(case.title,a))
        except Exception as e:
            print('请求注册接口失败：', e)
            self.logger.error('测试场景【{}】，测试是吧-请求注册接口失败：{}'.format(case.title, e))

    def tearDown(self):
        self.excel.save()
        self.excel.close()
        self.http_request.close()

    @staticmethod
    def mobile_phone():
        num_phone = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                     '188', '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
        start_phone = random.choice(num_phone)
        end_num = ''.join(random.sample(string.digits, 8))
        return start_phone + end_num

# if __name__ == '__main__':
#     print(RegisterTest.mobile_phone())
