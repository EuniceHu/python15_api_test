#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: test_recharge.py
  @time: 2019/04/18
  
  """

"""
测试用例类总结：
1:接口自动化，就是模拟客户端向客户发请求，先写一个HttpRequest的类，然后导入到test类中
新建一个HttpRequest类的对象
2：每一条case就是一条测试用例，所以要新建一个Case类，测试用例是写在Excel中，所以要对
Excel中的测试用例读取
3：在test类中，引用Do_excel的这个类，新建Do_excel的对象，引用get_cases方法
4：在test方法中，使用http_request发送request请求，断言期望结果与实际结果是否一致
"""

import unittest
from week_9.class_0416.common.Task_http_request import HttpRequest2
from week_9.class_0416.common import Auto_do_excel
from week_9.class_0416.common import contants
from ddt import ddt,data


@ddt
class RechargeTest(unittest.TestCase):
     #首先使用DoExcel这个类，读取文件，获得测试用例
     excel=Auto_do_excel.DoExcel(contants.case_file,'recharge')
     cases=excel.get_cases()

     @classmethod
     def setUpClass(cls):#实例化HttpRequest2()的对象
         cls.http_request=HttpRequest2()
     @data(*cases)
     def test_recharge(self,case):
         print(case.title)
         resp=self.http_request.request(case.method,case.url,case.data)
         actual_code=resp.json()['code']
         try:
             self.assertEqual(str(case.expected),actual_code)
             self.excel.write_result(case.case_id+1,actual_code,'pass')
         except AssertionError as e:
             self.excel.write_result(case.case_id+1,actual_code,'fail')
             raise e
     @classmethod
     def tearDownClass(cls):
         cls.http_request.close()








