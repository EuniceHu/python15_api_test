# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 9:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_知识补充.py
# 1：变量的范围  2：import 与main
# from week_3.class_0302.robot import robot
# robot('小蚂蚁','今天一起去shopping吗？')

# language='java'#全局变量

def coding():
    global language #声明这个language是一个全局变量
    language='python'#局部变量 只能在当前函数内部生效
    print('我最喜欢的代码是：{}'.format(language))
    language='ruby'

def automation_testing(type):
    print("{}自动化测试，用{}代码比较适合公司的框架".format(type,language))

coding()
automation_testing('app')

#全局变量  局部变量同名的话
#1：如果全局变量和局部变量同时存在的话 ，那么函数优先调用自己局部变量
#2：如果不存在局部变量，那么函数就调用全局变量
#3：global 变量名  声明是一个全局变量