# encoding=utf_8
# @Author  ： 豆子
import json
import unittest

from ddt import ddt, data

from douzi_0321.commons.testrequest import TestHttpRequest
from douzi_0323.commons import filepath
from douzi_0323.commons.excelparse import ExcelParse
from douzi_0323.commons.logprase import LogParse

ep = ExcelParse(filepath.data_dir)
cases = ep.get_cases('test_data')

COOKIES = None


@ddt
class RequestUnitTest(unittest.TestCase):

    @data(*cases)
    def test_api(self, case):
        global COOKIES
        param = json.loads(case['param'])
        req = TestHttpRequest(url=case['url'], method=case['method'], param=param, cookies=COOKIES)
        LogParse().info('响应结果信息{}'.format(req.get_json()))
        if req.get_cookies():
            COOKIES = req.get_cookies()
        try:
            self.assertEqual(str(case['excepted']), req.get_json_code())
            result = 'Pass'
        except AssertionError as a:
            result = 'Fail'
            raise a
        finally:
            ep.back_write_by_excel('test_data', case['case_id'], req.get_text(), result)
            LogParse().info('执行结果{}'.format(result))


if __name__ == '__main__':
    unittest.main()
