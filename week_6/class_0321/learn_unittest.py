# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 20:01
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_unittest.py

#主题：单元测试
#类：属性 方法
#属性  类属性 对象属性
#方法 类方法 静态方法 对象方法

#单元测试是谁的做的？--开发 ---不会写代码的测试
# 开发可以做 我也可以做

#单元测试是做什么--->对某个功能去做测试--->每一个功能都是封装在类里面--->类里面有方法和属性
#--->单元测试测试什么？--->方法--->创建对象 调用方法  传参--->通过传递多组数据来测试不同的情况

#框架--->unittest--->pytest
#python unittest 单元测试

#写用例 case TestCase 用来写用例
import unittest
from week_6.class_0321.math_method import MathMethod

class TestAdd(unittest.TestCase):#测试类

    #没有测试用例--我们来加
    #测试用例:test开头
    def test_001(self):#测试2个零相加
        print('test_add_two_zero')
        expected=0#期望值
        res=MathMethod().add(0,0)#实际值
        #断言
        self.assertEqual(expected,res)

    def test_002(self):#测试一正一负数字相加
        print('test_add_positive_negative')
        expected=-2#期望值
        res=MathMethod().add(1,-3)#实际值
        #断言
        self.assertEqual(expected,res)


#ASCII编码  用例执行的顺序
class TestSub(unittest.TestCase):#测试类--测试减法

    #没有测试用例--我们来加
    #测试用例:test开头
    def test_001(self):#测试2个零相加
        print('test_sub_two_zero')
        expected=0#期望值
        res=MathMethod().sub(0,0)#实际值
        #断言
        self.assertEqual(expected,res)

    def test_002(self):#测试一正一负数字相加
        print('test_sub_positive_negative')
        expected=4#期望值
        res=MathMethod().sub(1,-3)#实际值
        #断言
        self.assertEqual(expected,res)


if __name__ == '__main__':
    unittest.main