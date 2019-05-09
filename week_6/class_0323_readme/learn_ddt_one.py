#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: learn_ddt.py
  @time: 2019/03/24
  
  """
import unittest
from ddt import ddt,data,unpack

@ddt
class TestAdd(unittest.TestCase):


    #@data 装饰方法 ，跟for循环一样，遍历元祖的每个数据，然后传递给被修饰方法的参数
    # 有几条数据，就执行几次用例

    # @data(1,2,3,4)
    # def test_001(self,a):
    #     print(a)


    # @data([1,2],[3,4])#相当于元祖([1,2],[3,4]),遍历里面的元祖，是一个参数，所有传一个参数a
    # def test_001(self,a):
    #     print('a:',a)

    # @data(*[[1,2],[3,4]])#===([1,2],[3,4])--第一次遍历[1,2]  第二次遍历[3,4]
    # @unpack#[1,2] ====拆成2个参数1,2传递给test_001
    # def test_001(self,a,b):
    #     print('a:',a)
    #     print('b:',b)
    #元祖---1个元素----加*号，脱外套，把大列表去掉，里面是有2个元素


    # @data(*[{'a':0,'b':0,'expected':0},{'a':1,'b':1,'expected':1}])
    # @unpack#对字典进行拆分,（针对每一条用例的数据进行拆分）
    # def test_001(self,expected,a,b):#如果是字典的话 要用他的key作为参数来进行数据接收
    #     print('a:',a)
    #     print('b:',b)
    #     print('expected',expected)

    @data(*[[0,0,0,9],[1,1,1]])
    @unpack
    def test_001(self,a,b,c,d=None):
        print('a:',a)
        print('b:',b)
        print('c',c)
        print('d',d)

    #总结，data传进来的数据是元祖，遍历元祖里面的数据，有几条数据，就执行几条用例
    #加*号，就相当于脱外套，一个大列表里面嵌套列表，就把大列表脱掉，里面就只有小列表里面的数据
    #加unpack，相当于把小列表里面的元素按照逗号分隔，小列表里面有几个数据，就用几个参数胡来接收
    #data里面的数据传进来--元组，有1个元素-->执行1条用例--->data数据加*--->变成了元组 有2个元素--->执行2个用例
    #---加unpack 根据逗号来进行拆分，变成了3个参数---测试方法要用3个参数来进行接收




