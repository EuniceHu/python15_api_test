

#!/usr/bin/python3

# Author:xuqiao

# Time:2019/3/2318:00

# File:unittest_http_testcase.

# Email:1462942304@qq.com

from ddt import ddt,data,unpack

import unittest
from data import login_info
from http_helper import HttpGetPost
from xls import get_data, write_result

# @ddt
# @data
# @unpack

print(login_info)  # 列表 list

@ddt
class HttpTestCase(unittest.TestCase):

    """编写了四条用例，两条正确的，两条错误的"""

    @data(*get_data())
    @unpack
    def test_request(self,url,method,data,exp_data, case_id):
    # ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "get", {"mobilephone": 18688773467, "pwd": 123456},
    #      "登录成功"]
    # def test_request(self, login_info:list):

        print("请求地址是:{},请求的方式是：{}，传递的参数是：{}".format(url,method,data))
        # 实际结果
        res_data=HttpGetPost().http_request(url,method,data).json()
        # 实际结果 == 预期结果?? 断言
        try:
            self.assertEqual(exp_data,res_data["msg"])
        except AssertionError as e:
            # logging
            # 测试不通过的结果： “failed” 写到 Excel
            row = int(case_id) + 1
            write_result(row, "failed")



# 测试流程：设计测试用例： url:... method:... data:... 预期结果。。。
# 1. Excel
# 2. 配置文件。 ini .conf .propties /parse
# 3. txt
# 4. 变量。

if __name__ == '__main__':
    unittest.main()



