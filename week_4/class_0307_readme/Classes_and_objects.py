#-*- coding:utf-8 _*-
"""
  @author:小胡
  @file: Classes_and_objects.py
  @time: 2019/03/08
  
  """
#万物皆对象

#类的语法

# class 类名:
#     '''类的解释文档'''
    #1）类的方法：功能
    #2）类的属性：特征

#类名的规范：标识符 数字 字母 下划线组成 ，不能以数字开头
#见名知意   不能使用关键字   驼峰命名：每个单词首字母大写
# HuaHuaLemon  huaHuaLemon
# SaberLemon   saberLemon


#实际的男朋友类
#高 写代码 有车  会做饭  打篮球  sex=男
#怎么变成代码

# class BoyFriend:
#     '''这是一个男朋友类，主要是用来描述男朋友这一类人'''
#     #属性
#     sex='boy'
#     height=170
#
#     #方法--->90%的相似度--函数
#     def coding(self,language='python'):
#         print('会写{}代码，而且写的66的'.format(language))
#
#     def cooking(self,*args):
#         dish_name=''#初始字符串 空字符串
#         for item in args:#遍历args这个元组
#             dish_name+=item#遍历每个元素 之后 都加到dish_name这个字符串上去
#             dish_name+='、'#每个选项之间 加顿号隔开
#         print('会做饭，而且擅长做{}'.format(dish_name))
#
#     def play_basketball(self):
#         return '最喜欢打篮球'
#
# #万物皆对象--对象肯定是属于某个类--->类可以产生对象
# #创建对象：类名()
# t=BoyFriend()#一个对象
#
# #对象具有类的所有属性和方法   调用  对象.属性  对象.方法
# print(t.sex)
# print(t.height)
#
# t.coding()
# t.cooking('方便面','蛋炒饭','西红柿蛋汤')
# res=t.play_basketball()
# print(res)


# 手机：
# A 颜色  B 像素  C 听歌 D 打电话  E 发短信  F 上网  G尺寸大小

# t1=BoyFriend()
# t2=BoyFriend()
#
# print(id(t1))
# print(id(t2))



class GirlFriend:
    '''这是一个女朋友类，主要是描述女朋友这一类人'''


    #属性
    height=165
    hair='long'
    @staticmethod
    def shopping(self):
        print('最喜欢去购物了')

    def cooking(self,*args):
        dish_name=''#初始化字符串
        for item in args:
            dish_name+=item#遍历的每个元素，都加到字符串上
            dish_name+='、'
        print('会做饭，并且擅长做：{}'.format(dish_name))

    @classmethod
    def coding(cls,language='python'):
        print('最喜欢用{}语言做自动化代码了'.format(language))


t=GirlFriend()#创建一个对象
print(t.hair)
print(t.height)
t.cooking('麻辣烫','水煮鱼','串串')
GirlFriend.coding()
t.coding()
