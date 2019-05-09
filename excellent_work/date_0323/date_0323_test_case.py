#coding:utf-8
#@time : 2019/3/24 14:00
# @Author : apple
#@file : date_0323_test_case.py

#结合3-21号的作业添加ddt Html测试报告
# 1：测试数据结合ddt来使用
# 2：出具一份测试报告

import unittest
from homework.date_0323.http_request import HttpRequest
from ddt import ddt,data,unpack
from homework.date_0323.excel_read_and_write import ExcelReadAndWrite


@ddt#装饰TestCase的子类
class TestHttpRequest2(unittest.TestCase):#测试类，继承TestCase

    #读取测试用例表里的输入数据以及预期结果
    test_data = ExcelReadAndWrite('test_data.xlsx','Sheet1').read_excel(5,4,row_start_id=2)
    @data(*test_data)#装饰方法
    @unpack#拆分列表
    def test_001(self,url,method,param,expected):
        print('test_001')
        res=HttpRequest().http_request(url,method,eval(param)).get("code")#实际值
        print(str(expected),type(str(expected)))
        print(str(res),type(str(res)))
        #断言
        self.assertEqual(str(expected),str(res))

