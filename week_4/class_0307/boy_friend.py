# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 21:12
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : boy_friend.py

class BoyFriend:
    '''这是一个男朋友类，主要是用来描述男朋友这一类人'''
    #属性
    sex='boy'
    height=170

    #方法--->90%的相似度--函数
    @staticmethod#如果有一个这样的方法  它跟类里面的属性 函数 没有任何关联的时候  用不到他们
    def coding(language='python'):#静态方法跟普通函数100%的相似度
        print('会写{}代码，而且写的66的'.format(language))

    def cooking(self,*args):
        dish_name=''#初始字符串 空字符串
        for item in args:#遍历args这个元组
            dish_name+=item#遍历每个元素 之后 都加到dish_name这个字符串上去
            dish_name+='、'#每个选项之间 加顿号隔开
        print('会做饭，而且擅长做{}'.format(dish_name))

    @classmethod
    def play_basketball(cls):#调用这个方法的时候 会把类作为参数传进来--> @classmethod、cls类方法的特征
        print('最喜欢打篮球')
        print('我男朋友的性别是：{}'.format(cls.sex))
        cls.coding()
        cls().cooking()#

    def print_self(self):#对象方法：只能对象来调用---》self对象方法的标志特征
        print('self:',self)
        print('我男朋友的身高是:{}'.format(self.height))
        self.cooking('辣椒炒肉','麻辣烫')
        self.play_basketball()
        self.coding()


#self---调用这个方法的对象本身
#在类外面：类里面的属性和方法 谁可以调用？--->对象
# x=BoyFriend()
# x.print_self()
# print('   x:',x)
# BoyFriend().print_self()

#对象方法：必须是由对象来进行调用---只有它不同！！！！
#类方法：类可以调用 对象可以调用 @classmethod 装饰
# BoyFriend.play_basketball()
# BoyFriend().play_basketball()
#静态方法：类可以调用 对象可以调用 @staticmethod 装饰
# BoyFriend.coding()#类调用
# BoyFriend().coding()#对象调用

#下节课再解密！
#为什么会有对象方法  类方法 静态方法？我什么时候写什么类型的方法呢？
#什么时候用？
#写成不同的方法类型 有啥用呢？对我来说有啥用?

#他们有什么区别呢？
#自己总结一波。

# t=BoyFriend()
# t.print_self()
# BoyFriend.play_basketball()
BoyFriend.cooking(BoyFriend(),'kkk','lll')
BoyFriend.cooking('hhh','kkk','lll')