#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: test_register.py
  @time: 2019/04/22
  
  """
# import unittest
# from week_9.class_0416.common.Task_http_request import HttpRequest2
# from week_9.class_0416.common import Auto_do_excel
# from week_9.class_0416.common import contants
# from ddt import ddt,data
#
# @ddt
# class RegisterTest(unittest.TestCase):
#     excel=Auto_do_excel.DoExcel(contants.case_file,'register')#实例化DoExcel的类，读取文件，调用get_cases的方法
#     cases=excel.get_cases()
#
#     @classmethod
#     def setUpClass(cls):
#         cls.http_request=HttpRequest2()#新建一个HttpRequest2()的实例
#     @data(*cases)
#     def test_register(self,case):
#         #发送httprequests的请求
#         resp=self.http_request.request(case.method,case.url,case.data)
#         try:
#             self.assertEqual(case.expected,resp.text)
#             self.excel.write_result(case.case_id+1,resp.text,'pass')
#         except AssertionError as e:
#             self.excel.write_result(case.case_id+1,resp.text,'fail')
#             raise e
#
#     @classmethod
#     def tearDownClass(cls):
#      cls.http_request.close()


