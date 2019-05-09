#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Knowledge.py
  @time: 2019/03/02
  
  """
# from week_3.class_0302_readme.robot import *
# robot("002","我们一起哈哈哈哈")

# language='c#'#全局变量

def coding():
    global language#声明这个language是一个全局变量
    language='python'#局部变量 只能在当前函数内部生效
    # print(id(language))
    print('我最喜欢的代码是：{}'.format(language))
    language='ruby'#重新赋值给ruby




def automation_testing(type):
    print("{}自动化测试，用{}代码比较适合公司的框架".format(type, language))

coding()
automation_testing('app')


#全局变量  局部变量同名的话
#1：如果全局变量和局部变量同时存在的话 ，那么函数优先调用自己局部变量
#2：如果不存在局部变量，那么函数就调用全局变量
#3：global 变量名  声明是一个全局变量