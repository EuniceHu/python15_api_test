#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: test_register.py
  @time: 2019/04/22
  
  """
import unittest
from week_9.class_0419.common.Task_http_request import HttpRequest2
from week_9.class_0419.common import Auto_do_excel
from week_9.class_0419.common import contants
from ddt import ddt,data
from week_9.class_0419.common import do_mysql

@ddt
class RegisterTest(unittest.TestCase):
    excel=Auto_do_excel.DoExcel(contants.case_file,'register')#实例化DoExcel的类，读取文件，调用get_cases的方法
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HttpRequest2()#新建一个HttpRequest2()的实例
        cls.mysql=do_mysql.DoMysql()


    @data(*cases)
    def test_register(self,case):
        if case.data.find('register_mobile')>-1:
            sql='select mobilephone from future.member where mobilephone = "13037680161";'
            min_phone=self.mysql.fetch_one(sql)[0]#查询最大手机号码
            #最大手机号码+1
            min_phone=int(min_phone)+11
            print('最大手机号码',min_phone)
            #最大手机号码替换参数值
            case.data=case.data.replace('register_mobile',str(min_phone))

        #发送httprequests的请求
        resp=self.http_request.request(case.method,case.url,case.data)
        print('替换之后的case_data是：',case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,'pass')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'fail')
            raise e



    @classmethod
    def tearDownClass(cls):
     cls.http_request.close()
     cls.mysql.close()


