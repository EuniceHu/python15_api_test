# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 9:39
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task_0307.py
# 2:建一个名为 User 的类，其中包含属性 first_name 和 last_name，
# 还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。

class User:

    #属性
    first_name='华华'
    last_name='刘'

    #方法
    def describe_user(self):
        '''打印用户的信息摘要'''
        print('我的名字是{}{}'.format(self.last_name,self.first_name))

    def greet_user(self,name,content='早上好'):#位置参数  默认参数
        print('{},{}'.format(name,content))

if __name__ == '__main__':
    t=User()
    t.describe_user()
    t.greet_user('saber','到底听懂了没有！')#saber-->name