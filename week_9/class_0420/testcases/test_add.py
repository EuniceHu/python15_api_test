#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: test_add.py
  @time: 2019/04/24
  
  """
"""
编写测试用例
第一先导入unittest
第二导入发送request请求的模块
第三导入读取excel的模块
第四导入路径的模块
第五导入ddt
第六执行不成功入的一个坑，就是在配置文件中添加新的配置，但是导入的模块，还是之前的模块，
要想使用新增加的配置，导入包的时候，路径要修改，你使用之前的路径时候，新增加的配置文件中的section就会读取不到
"""
import unittest
from week_9.class_0420.common.Task_http_request import HttpRequest2
from week_9.class_0420.common import Auto_do_excel
from week_9.class_0420.common import contants
from ddt import ddt,data
from week_9.class_0420.common.config import config
from week_9.class_0420.common import context

@ddt
class AddTest(unittest.TestCase):
     excel=Auto_do_excel.DoExcel(contants.case_file,'add')
     cases=excel.get_cases()

     @classmethod
     def setUpClass(cls):
         cls.http_request=HttpRequest2()
     @data(*cases)
     def test_add(self,case):

         # case.data = eval(case.data)#变成字典
         # if case.data.__contains__('mobilephone') and case.data['mobilephone']== 'normal_user' :
         #     case.data['mobilephone'] = config.get('data','normal_user')
         #     #拿到配置文件里面的值赋值给mobilephone
         # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
         #     case.data['pwd'] = config.get('data', 'normal_pwd')
         # if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
         #     case.data['memberId'] = config.get('data', 'loan_member_id')
         #在请求之前，替换参数化的值
         case.data=context.replace(case.data)
         resp=self.http_request.request(case.method,case.url,case.data)
         try:
             self.assertEqual(str(case.expected),resp.json()['code'])
             self.excel.write_result(case.case_id+1,resp.text,'pass')
         except AssertionError as e:
             self.excel.write_result(case.case_id+1,resp.text,'fail')
             raise e

     @classmethod
     def tearDownClass(cls):
        cls.http_request.close()

