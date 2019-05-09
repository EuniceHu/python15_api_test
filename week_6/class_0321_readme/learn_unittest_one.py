#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: learn_unittest.py
  @time: 2019/03/21
  
  """
#主题：单元测试
#类：属性 方法
#属性  类属性 对象属性
#方法 类方法 静态方法 对象方法

#单元测试是谁的做的？--开发 ---不会写代码的测试
# 开发可以做 我也可以做

#单元测试-->就是对某个功能去做测试-->每一个功能都是封装在类里面-->类里面有属性和方法
#单元测试主要测的是什么？-->方法-->创建对象，调用方法  传参--->通过传递多组数据来测试不同的情况

#写用例 Case TestCase

import unittest
from week_6.class_0321_readme.math_add_sub import MathMethod
#导入数学类，编写数学类的测试用例

class TestAdd(unittest.TestCase):#测试加法类
    #我们添加测试用例，测试用例必须要用test开头

   def test_001(self):#测试2个0相加
       print('test_add_two_zero')
       expected=0#期望值
       res=MathMethod().add(0,0)#实际值
       self.assertEqual(expected,res)#断言 期望值和实际值是否相等

   def test_002(self):#测试一正一负数字相加
       print('test_add_positive_negative')
       expected=-2
       res=MathMethod().add(1,-3)
       self.assertEqual(expected,res)



class TestSub(unittest.TestCase):

    def test_001(self):
        print('test_sub_two_zero')
        expected=0#期望值
        res=MathMethod().sub(0,0)#实际值
        self.assertEqual(expected,res)
    def test_002(self):
        print('test_sub_positive_negative')
        expected=4
        res=MathMethod().sub(a=1,b=-3)
        self.assertEqual(expected,res)


if __name__ == '__main__':
    unittest.main

