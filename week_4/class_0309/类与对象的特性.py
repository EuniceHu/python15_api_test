# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:44
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 类与对象的特性.py

#继承 拓展 重写

#新一代手机  新加支付功能
from week_4.class_0309.类与对象 import Phone
class Phone_1(Phone):#括号里面的是父类 Phone_1 是子类

    def __init__(self,color):#如果子类有自己的初始化，就不用继续使用父类的初始化
        self.color=color

    def phone_info(self):#重写--父类有  子类重新写
        #如果子类与父类有重名方法，那么子类的操作就叫重写方法 override
        #生效范围 在这个子类里面
        print('这是一款智能手机！')

    def pay(self):#支付功能===》子类的方法  子类的拓展
        #如果子类里面有父类里面没有的方法，那么子类的操作就叫做拓展
        print('可以支付')


#爸爸的就是我的  我的还是我的
#继承：子类可以拥有父类里面的所有所有属性、所有方法--->就可以直接调用
if __name__ == '__main__':#导入模块  文件对象  路径操作的时候 都讲过
    t=Phone_1('red')
    # t.call('15096090550')
    # t.pay()
    t.phone_info()
    t.take_shoot()

    #对象=类名()
    # t1=Phone_1()
    # t2=Phone('red','2300','vivo',6.5)
    #
    # t1.phone_info()
    # t2.phone_info()



