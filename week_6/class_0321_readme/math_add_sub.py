#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: math_add_sub.py
  @time: 2019/03/22
  
  """

class MathMethod:
    '''一个数学类，2个方法 一个是加法 一个是减法'''

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

if __name__ == '__main__':
    MathMethod().add(1,2)